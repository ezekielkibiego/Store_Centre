from django.conf import settings
from django.shortcuts import redirect, render
from transport.models import *
from transport.forms import *
from django.contrib.auth.decorators import login_required
import requests,json

@login_required(login_url='client_login')
def request_transport(request):
    api_key = settings.GOOGLE_API_KEY
    if request.method == 'POST':
        form = TransportForm(request.POST)
        if form.is_valid():
            transport_request = form.save(commit=False)
            transport_request.user = request.user
            #distance matrix logic
            source = 'Moringa School,Nairobi,Kenya'
            destination = transport_request.address
            url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
            r = requests.get(url + 'origins=' + source +
                   '&destinations=' + destination +
                   '&key=' + api_key)
            x=r.json()
            print(x['rows'][0]["elements"][0]['distance']["value"])
            transport_request.distance = x['rows'][0]["elements"][0]['distance']["value"]
            transport_request.save()
            print("transport:", transport_request.distance)
            return redirect('request_summary')
        else:
            print(form.errors)
    else:
        form =TransportForm()
    context = {
        'form':form,
        'api_key': api_key
    }
    return render(request,'request_transport.html', context)

@login_required(login_url='client_login')
def request_summary(request):
    request_transport = Transport.objects.filter(user=request.user).last()
    print(request_transport.user.first_name)
    context = {
        'request_transport': request_transport,
    }
    return render(request,'request_summary.html', context)
