from django.conf import settings
from django.shortcuts import redirect, render
from transport.models import *
from transport.forms import *
from django.contrib.auth.decorators import login_required
import requests,json
import re
from django_daraja.mpesa.core import MpesaClient
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from django.urls import reverse
from requests.api import get
from requests.auth import HTTPBasicAuth




@login_required(login_url='client_login')
def request_transport(request):
    api_key = settings.GOOGLE_API_KEY
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
            transport_request.save()
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


@login_required(login_url='client_login')
def summaries(request):
    summaries = Transport.objects.filter(user=request.user).all().order_by('-created')
    
    print(summaries)
    context = {
        'summaries': summaries,
    }
    return render(request,'summaries.html', context)



cl = MpesaClient()
stk_push_callback_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
b2c_callback_url = 'https://sandbox.safaricom.co.ke/mpesa/b2c/v1/paymentrequest'
c2b_callback_url = 'https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl'

def getAccessToken(request):
    consumer_key = 'GAeIsGiTzoclVjKZ0lpGkRTKqSOlM4tP'
    consumer_secret = 'il1gZPOjXMF3LeFD'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    return HttpResponse(validated_mpesa_access_token)

def oauth_success(request):
	r = cl.access_token()
	return JsonResponse(r, safe=False)
    

def stk_push_success(request, ph_number, totalAmount):
    phone_number = ph_number
    amount = totalAmount
    account_reference = 'Store Centre'
    transaction_desc = 'STK Push Description'
    callback_url = stk_push_callback_url
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)



@login_required(login_url='client_login')
def payment(request):
    request_transport = Transport.objects.filter(user=request.user).last()
    request_goods = Goods.objects.filter(owner=request.user).last()  
    context = {
        'request_transport': request_transport,
        'request_goods': request_goods,
        
    }
    if request.method == 'POST':
        name=request.POST.get('fname')
        phone_number=request.POST.get('phone_number')
        amount=request.POST.get('amount')

        ph_number = None
        totalAmount = int(float(amount))

        if phone_number[0] == '0':
            ph_number = '254'+ phone_number[1:]
        elif phone_number[0:2] == '254':
            ph_number = phone_number
        else:
            # messages.error(request, 'Check you Phone Number format 2547xxxxxxxx')
            return redirect(request.get_full_path())


        stk_push_success(request, ph_number, totalAmount)

        return render (request,'success.html')


    return render(request,'payment.html', context)
