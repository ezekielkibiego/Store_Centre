from django.shortcuts import render
from transport.forms import *

def request_transport(request):
    form= TransportForm()
    context = {
        'form':form
    }
    return render(request,'request_transport.html', context)
