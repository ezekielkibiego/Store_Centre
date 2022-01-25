from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render
from analytics.models import Order
from django.core import serializers
from django.contrib.auth.decorators import login_required

@login_required(login_url = '/admin_login')
def dashboard_with_pivot(request):
    current = request.user
    if current.is_staff:
        return render(request, 'staff_dashboard.html', {})



def pivot_data(request):
    dataset = Order.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)


    # def client_login(request):
    # if request.method=='POST':
    #     form = AuthenticationForm(data=request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data.get('username')
    #         password = form.cleaned_data.get('password')
    #         user = authenticate(username=username, password=password)
    #         if user is not None :
    #             login(request,user)
    #             return redirect('/')
    #         else:
    #             messages.error(request,"Invalid username or password")
    #     else:
    #             messages.error(request,"Invalid username or password")
    # return render(request, 'client_login.html',
    # context={'form':AuthenticationForm()})


