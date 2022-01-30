
from django.conf import settings
from django.shortcuts import redirect, render
from transport.models import *
from transport.forms import *
from django.contrib.auth.decorators import login_required
import requests,json
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage

@login_required(login_url='client_login')
def request_transport(request):
    api_key = settings.GOOGLE_API_KEY
    initial_units=request.session.get('initial_units')
    final_units = request.session.get('final_units')
    if request.method == 'POST':
        form = TransportForm(request.POST)
        if form.is_valid():
            transport_request = form.save(commit=False)
            transport_request.user = request.user
            #client goods logic
            goods = Goods.objects.filter(owner=request.user).last()
            transport_request.goods= goods
            #distance matrix logic
            source = 'Moringa School,Nairobi,Kenya'
            destination = transport_request.address
            url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
            r = requests.get(url + 'origins=' + source +
                '&destinations=' + destination +
                '&key=' + api_key)
            x=r.json()
            print(x)
            distance = x['rows'][0]["elements"][0]["distance"]["value"]
            transport_request.distance = (distance)/1000
            #calculate price
            price = (transport_request.distance)*200
            transport_request.price = price
            #transport_type logic
            if initial_units > final_units:
                transport_request.transport_type = Transport.PICKUP
            elif final_units > initial_units:
                transport_request.transport_type= Transport.DELIVERY
            transport_request.save()
            return redirect('request_summary')
        else:
            print(form.errors)
    else:
        form =TransportForm()
    context = {
        'form':form,
        'api_key': api_key,
        'initial_units':initial_units,
        'final_units': final_units,
    }
    return render(request,'request_transport.html', context)

@login_required(login_url='client_login')
def request_summary(request):
    request_transport = Transport.objects.filter(user=request.user).last()
    
    print(request_transport.user.first_name)
    context = {
        'request_transport': request_transport,
    }
    
    #email logic
    subject = 'TRANSPORT REQUEST SUMMARY'
    message = get_template('transport_summary_email.html').render(context)
    msg = EmailMessage(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [request_transport.email],
    )
    msg.content_subtype = 'html'
    msg.send()
    
    return render(request,'request_summary.html', context)


@login_required(login_url='client_login')
def summaries(request):
    summaries = Transport.objects.filter(user=request.user).all().order_by('-created')
    context = {
        'summaries': summaries,
    }
    
    
    return render(request,'summaries.html', context)

@login_required(login_url='client_login')
def payment(request):
    request_transport = Transport.objects.filter(user=request.user).last()
    request_goods = Goods.objects.filter(owner=request.user).last()  
    context = {
        'request_transport': request_transport,
        'request_goods': request_goods,
        
    }
    return render(request,'payment.html', context)
