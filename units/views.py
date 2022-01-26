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
            goods_booking = form.save(commit=False)
            storage_type= form.cleaned_data.get('storage_type')
            no_of_units= form.cleaned_data.get('no_of_units') # available units
            units = Storage.objects.filter(type=storage_type).all() # total units
            print(no_of_units)
            print(units)
            print(storage_type)
            if units.available_units >= no_of_units:
                goods_booking.owner = request.user

                # goods_booking.unit_no = available_units[0]
                # booked_unit = Unit.objects.filter(pk = available_units[0].pk ).first()
               
                # booked_unit.booked = True
                # booked_unit.add_unit()
                
                goods_booking.save()
                storage = Storage.objects.filter(type=storage_type).first()
                storage.available_units -= no_of_units
                storage.add_storage() 
                
            else:
                messages.error(request,f'No slots available in {storage_type} try again later')
                return redirect('book')
        else: 
            print('Not  worrkighjn')
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
    normal_units = Storage.objects.filter(type='normal_storage')
    booked_normal_units = Storage.objects.filter(type='normal_storage').count()
    bonded_units = Storage.objects.filter(type='bonded_storage')
    booked_bonded_units = Storage.objects.filter(type='bonded_storage').count()
    archive_units = Storage.objects.filter(type='archive_storage')
    booked_archive_units = Storage.objects.filter(type='archive_storage').count()
    hazardious_units = Storage.objects.filter(type='hazardious_storage')
    booked_hazardious_units = Storage.objects.filter(type='hazardious_storage').count()
    cold_units = Storage.objects.filter(type='cold_storage')
    booked_cold_units = Storage.objects.filter(type='cold_storage').count()
    
    if request.method == 'POST':
        form = StorageForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('dashboard')
    else:
        form = StorageForm()


        args = {
            "normal_units": normal_units,
            "booked_normal_units":booked_normal_units,
            "bonded_units": bonded_units,
            "booked_bonded_units":booked_bonded_units,
            "archive_units": archive_units,
            "booked_archive_units":booked_archive_units,
            "hazardious_units": hazardious_units,
            "booked_hazardious_units":booked_hazardious_units,
            "cold_units": cold_units,
            "booked_cold_units":booked_cold_units,
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

