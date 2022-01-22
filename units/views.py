from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from transport.models import *
from .forms import UnitForm,GoodsBookingForm
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url = '/client_login')
def book_unit(request):
    
    if request.method == 'POST':
        form = GoodsBookingForm(request.POST)
        if form.is_valid():
            goods_booking = form.save(commit=False)
            storage_type= form.cleaned_data.get('storage_type')
            available_units = Unit.objects.filter(type=storage_type,booked=False)
            if available_units is not None:
                goods_booking.owner = request.user
                goods_booking.unit_no = available_units[0]
                booked_unit = Unit.objects.filter(pk = available_units[0].pk ).first()
               
                booked_unit.booked = True
                booked_unit.add_unit()
                
                goods_booking.save()
            else:
                print('no slots available')
                
        return redirect('book')
    else:
        form = GoodsBookingForm()

    context = {
        
        "form": form
    }
    return render(request,'booking.html',context)

def dashboard(request):
    normal_units = Unit.objects.filter(type='normal_storage')
    bonded_units = Unit.objects.filter(type='bonded_storage')
    archive_units = Unit.objects.filter(type='archive_storage')
    hazardious_units = Unit.objects.filter(type='hazardious_storage')
    cold_units = Unit.objects.filter(type='cold_storage')

    args = {
        "normal_units": normal_units,
        "bonded_units": bonded_units,
        "archive_units": archive_units,
        "hazardious_units": hazardious_units,
        "cold_units": cold_units,
    }
    return render(request,'staff_dashboard.html',args)

def display_units(request,storage_type):

    units = Unit.objects.filter(type=storage_type,booked=True)
   

    if request.method == 'POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('units',storage_type)
    else:
        form = UnitForm()

    context = {
        "units": units,
        "form": form
    }

    return render(request,'units.html',context)

