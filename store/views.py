from django.shortcuts import redirect, render,HttpResponse
from django.contrib import messages
from store.forms import ClientSignUpForm
from .models import *
from units.models import *
from django.contrib.auth import authenticate, login, logout
from . import *
from datetime import date
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def IndexView(request):
    return render(request, 'index.html')


@login_required(login_url = '/client_login')
def records(request):
    storage_records = Goods.objects.filter(owner=request.user).all
    print(type(storage_records))

    return render(request, "records.html",{'records':storage_records})

def services(request):
    
    
    return render(request, "services.html")



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
        login(self.request, user)
        return redirect('/')


class staff_register(CreateView):
    model = User
    form_class = StaffSignUpForm
    template_name = 'staff_registration.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

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
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'staff_login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')

