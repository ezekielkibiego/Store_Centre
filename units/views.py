import re
from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from transport.models import *
from .forms import StorageForm,GoodsBookingForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url = '/client_login')
def book_unit(request):
    
    if request.method == 'POST':
        form = GoodsBookingForm(request.POST)
        if form.is_valid():
            
            storage_type= form.cleaned_data.get('storage_type')
            arrival_date= form.cleaned_data.get('arrival_date')
            departure_date= form.cleaned_data.get('departure_date')
            description = form.cleaned_data.get('description')
            no_of_units= form.cleaned_data.get('no_of_units') # available units
            total_cost = form.cleaned_data.get('total_cost') 
        
            
            units = Storage.objects.filter(type=storage_type).first() 
            if units.available_units >= no_of_units:
                storage =  get_object_or_404(Storage,type=storage_type)
                booked_unit =  Goods(storage_type =storage,no_of_units=no_of_units,arrival_date=arrival_date,departure_date=departure_date,description =description,owner =request.user,total_cost=total_cost)
                booked_unit.add_goods()
                storage = Storage.objects.filter(type=storage_type).first()
                storage.available_units -= no_of_units
                storage.add_storage() 
                messages.success(request,f'Booked successfully')
                
            else:
                messages.error(request,f'No slots available in {storage_type} try again later')
                return redirect('book')
        else: 
            messages.error(request,f'Something went wrong')
            return redirect('book')

        return redirect('request_transport')
    else:
        form = GoodsBookingForm()
        storage_types = Storage.objects.all()

    context = {
        
        "form": form,
        "storage_types": storage_types
    }
    return render(request,'booking.html',context)

def dashboard(request):
    storages = Storage.objects.filter()
    
    if request.method == 'POST':
        form = StorageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Booked successfully')
        else:
            messages.error(request,'Something went wrong')
        return redirect('dashboard')
            
    else:
        form = StorageForm()


        args = {
            "storages": storages,
            "form":form
        }
        return render(request,'staff_dashboard.html',args)

def display_units(request,storage_type):

    
    goods = Goods.objects.filter(storage_type=storage_type)

    form = StorageForm()

    context = {
        "goods": goods,
        "storage_type":storage_type,
    }

    return render(request,'units.html',context)

