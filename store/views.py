from cProfile import Profile
from http import client
from django.shortcuts import redirect, render,HttpResponse
from django.contrib import messages
from store.forms import ClientSignUpForm,SubscribeForm
from .models import *
from units.models import *
from django.contrib.auth import authenticate, login, logout
from . import *
from datetime import date
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Storecentre
from .serializers import StoreSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
class Storelist(APIView):
    def get(self, request, format=None):
        all_store = Storecentre.objects.all()
        serializers = StoreSerializer(all_store, many=True)
        return Response(serializers.data)
def post(self, request, format=None):
        serializers = StoreSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
permission_classes = (IsAdminOrReadOnly,)



def IndexView(request):
    form = SubscribeForm()
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subject = 'Store Centre'
            message = 'Welcome to Store Centre, All yor storage problems sorted by a click of a button.'
            recipient = form.cleaned_data.get('email')
            send_mail(subject, 
              message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            messages.success(request, 'Success!')
            return redirect('subscribe')
    return render(request, 'index.html',{'form': form})


@login_required(login_url = '/client_login')
def records(request):
    storage_records = Goods.objects.filter(owner=request.user).all
    print(type(storage_records))

    return render(request, "records.html",{'records':storage_records})

@login_required(login_url = '/client_login')
def services(request):
    
    storages = Storage.objects.all()
    return render(request, "services.html",{'storages':storages})



def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:

                return redirect("/admin")

            else:
                return HttpResponse("You are not an admin.")
        else:
            alert = True
            return render(request, "admin_login.html", {'alert':alert})
    return render(request, "admin_login.html")

def change_password(request):
    if request.method == "POST":
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(current_password):
                u.set_password(new_password)
                u.save()
                alert = True
                return render(request, "change_password.html", {'alert':alert})
            else:
                currpasswrong = True
                return render(request, "change_password.html", {'currpasswrong':currpasswrong})
        except:
            pass
    return render(request, "change_password.html")

def Logout(request):
    logout(request)
    return redirect ("/")


def register(request):
    return render(request, 'register.html')

class client_register(CreateView):
    model = User
    form_class = ClientSignUpForm
    template_name = 'client_registration.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('/client_login')


# def signup_view(request):
#     if request.method=='POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user=form.save()
#             login(request, user, backend='django.contrib.auth.backends.ModelBackend')
#             return redirect('home')



class staff_register(CreateView):
    model = User
    form_class = StaffSignUpForm
    template_name = 'staff_registration.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/staff_login')

def client_login(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'client_login.html',
    context={'form':AuthenticationForm()})

def staff_login(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('/analytics')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'staff_login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required(login_url = '/client_login')
def client_profile(request):
    current_user = request.user
    profile = Client.objects.get(user_id=current_user.id) 
    return render(request, "profile.html", {"profile": profile})

@login_required(login_url = '/staff_login')
def staff_profile(request):
    current_user = request.user
    profile = Staff.objects.filter(user_id=current_user.id).first()
    return render(request, "profile.html", {"profile": profile})


@login_required(login_url = '/admin_login')
def admin_profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    return render(request, "profile.html", {"profile": profile})


def update_client_profile(request):
  if request.method == 'POST':
    user_form = UpdateUserProfile(request.POST,request.FILES,instance=request.user)
    form = UpdateClientProfile(request.POST,request.FILES,instance=request.user)
    if user_form.is_valid() and form.is_valid():
      user_form.save()
      form.save()
      messages.success(request,'Your Profile account has been updated successfully')
      return redirect('profile')
  else:
    user_form = UpdateUserProfile(instance=request.user)
    form = UpdateClientProfile(instance=request.user) 
  params = {
    'user_form':user_form,
    'form':form
  }
  return render(request,'edit_profile.html',params)


# def staffProfile(request):
#     staff = request.user
#     profile = Staff.objects.get(
#         user_id=staff.id)  # get profile
#     profile = Staff.objects.filter(user_id = staff.id).first()  # get profile
#     context = {
#         "staff": staff,
#         'profile':profile
#     }
#     return render(request, 'profile.html', context)

def update_staff_profile(request):
    if request.method == 'POST':
        u_form = UpdateUserProfile(request.POST, request.FILES, instance=request.user)
        p_form = UpdateStaffProfile(request.POST, instance=request.user)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(
                request, 'Your Profile account has been updated successfully')
            return redirect('profile')
    else:
        u_form = UpdateUserProfile(instance=request.user)
        p_form = UpdateStaffProfile(instance=request.user)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request,'staff_profile.html',context)



def checkout_booking(request,records_id):
    goods = Goods.objects.filter(id=records_id).first()
    
    return render(request,'checkout.html',{'goods':goods})

def checkout_goods(request,goods_id):
    goods = Goods.objects.filter(id=goods_id).first()
    goods.remove_goods()
    storage = Storage.objects.filter(type =goods.storage_type).first()
    storage.available_units += goods.no_of_units
    storage.add_storage()
    messages.success(request,'Goods checked out successfully')
    
    
    return redirect('request_transport')

def subscribe(request):
    form = SubscribeForm()
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subject = 'Store Centre'
            message = 'Welcome to Store Centre, All yor storage problems sorted by a click of a button.'
            recipient = form.cleaned_data.get('email')
            send_mail(subject, 
              message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            messages.success(request, 'Success!')
            return redirect('subscribe')
    return render(request, 'index.html', {'form': form})

