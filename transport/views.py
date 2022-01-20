from django.shortcuts import redirect, render
from transport.models import *
from transport.forms import *

def request_transport(request):
    if request.method == 'POST':
        form = TransportForm(request.POST)
        if form.is_valid():
            transport_request = form.save(commit=False)
            transport_request.user = request.user
            transport_request.save()
        else:
            pass
    else:
        form =TransportForm(request.user)
    context = {
        'form':form
    }
    return render(request,'request_transport.html', context)

def request_summary(request):
    transport_request = Transport.objects.filter(user=request.user).last()
    context = {
        'transport_request': transport_request,
    }
    return render(request,'request_summary.html', context)
