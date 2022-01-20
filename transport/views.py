from django.shortcuts import redirect, render
import transport
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
