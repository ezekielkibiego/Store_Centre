
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django import forms
from store.models import *
from django.forms import ModelForm


class ClientSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    location = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User


    @transaction.atomic
    def save(self):
            user = super().save(commit=False)
            user.is_client = True
            user.first_name = self.cleaned_data.get('first_name')
            user.last_name = self.cleaned_data.get('last_name')
            user.save()
            client = Client.objects.create(user=user)
            client.email = self.cleaned_data.get('email')
            client.phone = self.cleaned_data.get('phone')
            client.location = self.cleaned_data.get('location')
            client.save()

            return client

class StaffSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    designation = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User


    @transaction.atomic
    def save(self):
            user = super().save(commit=False)
            user.is_staff = True
            user.first_name = self.cleaned_data.get('first_name')
            user.last_name = self.cleaned_data.get('last_name')
            user.save()
            staff = Staff.objects.create(user=user)
            staff.email = self.cleaned_data.get('email')
            staff.phone = self.cleaned_data.get('phone')
            staff.designation = self.cleaned_data.get('designation')
            staff.save()

            return staff

# class ProfileForm(ModelForm):
#     class Meta:
#         model = Profile
#         exclude = ['user']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class UpdateClientProfile(forms.ModelForm):
    class Meta:
        model = Client
        exclude = ['user']

class UpdateUserProfile(forms.ModelForm):
  class Meta:
    model = Client
    exclude = ['user']

class UpdateStaffProfile(forms.ModelForm):
    class Meta:
        model = Staff
        exclude = ['user']

class SubscribeForm(forms.Form):
    email = forms.EmailField()