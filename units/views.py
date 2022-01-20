from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import UnitForm,GoodsBookingForm

# Create your views here.
def book_unit(request):
    if request.method == 'POST':
        form = GoodsBookingForm(request.POST)
        if form.is_valid():
            goods_booking = form.save(commit=False)
            goods_booking.user = request.user
            goods_booking.save()

            pick_up = form.cleaned_data.get['pick_up']
            location = form.cleaned_data.get['location']
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

    units = Unit.objects.filter(type=storage_type,booked=False)
   

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

