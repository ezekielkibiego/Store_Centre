from inspect import Attribute
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Unit,Goods

class UnitForm(forms.ModelForm):
    
    type = forms.ChoiceField(choices=[('normal_storage','normal_storage'),('cold_storage','cold_storage'),('bonded_storage','bonded_storage'),('hazardious_storage','hazardious_storage'),('archive_storage','archive_storage')])

    class Meta:
        model = Unit
        fields = ('type','charge')

class GoodsBookingForm(forms.ModelForm):

    storage_type = forms.ChoiceField(choices=[('normal_storage','normal_storage'),('cold_storage','cold_storage'),('bonded_storage','bonded_storage'),('hazardious_storage','hazardious_storage'),('archive_storage','archive_storage')])
    
    class Meta:
        model = Goods
        fields = ('storage_type','description','arrival_date','departure_date')
        widgets = {
            'arrival_date':forms.DateInput(attrs={'type':'date'}),
            'departure_date':forms.DateInput(attrs={'type':'date'}),
           }
           