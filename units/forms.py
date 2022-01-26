from inspect import Attribute
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Goods,Storage
from django.forms.widgets import Select, SelectMultiple




class SelectWOA(Select):
    """
    Select With Option Attributes:
        subclass of Django's Select widget that allows attributes in options, 
        like disabled="disabled", title="help text", class="some classes",
              style="background: color;"...

    Pass a dict instead of a string for its label:
        choices = [ ('value_1', 'label_1'),
                    ...
                    ('value_k', {'label': 'label_k', 'foo': 'bar', ...}),
                    ... ]
    The option k will be rendered as:
        <option value="value_k" foo="bar" ...>label_k</option>
    """

    def create_option(self, name, value, label, selected, index, 
                      subindex=None, attrs=None):
        if isinstance(label, dict):
            opt_attrs = label.copy()
            label= opt_attrs.pop('label')
        else: 
            opt_attrs = {}
        option_dict = super(SelectWOA, self).create_option(name, value, 
            label, selected, index, subindex=subindex, attrs=attrs)
        for key,val in opt_attrs.items():
            option_dict['attrs'][key] = val
        return option_dict


class StorageForm(forms.ModelForm):


    class Meta:
        model = Storage
        fields = ('type','charge','no_units','available_units')

class GoodsBookingForm(forms.Form):
    storages = Storage.objects.all()
    choices =[( storage,{'label':storage.type,'charge':storage.charge }) for storage in storages]
    # choicess = [('b', 'blue'),
    #        ('g', {'label': 'green', 'disabled': 'disabled','value':'purple'}),
    #        ('c', {'label': 'cyan', 'title': 'Kind of violet', 'style': 'background: cyan;', }),
    #        ('r', 'red'), ]

    storage_type = forms.ChoiceField(choices=choices, label="storage",widget=SelectWOA)
    description = forms.CharField(widget=forms.TextInput(attrs={'style':"border-radius: 5px;" ,'name':"description", 'id':"description",'class':"form-control" ,'cols':"30", 'rows':"10" }))
    no_of_units =forms.IntegerField(widget=forms.NumberInput(attrs={'type':"number",'min':"1",'name':"no_of_units", 'id':"no_of_units", 'placeholder':"number of units"}))
    arrival_date =forms.DateField(widget=forms.DateInput(attrs={'type':'date','class':"form-control" ,'type':"date" ,'oninput':"total()", 'name':"arrival_date", 'id':"arrival_date"}))
    departure_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date','class':"form-control" ,'type':"date" ,'oninput':"total()", 'name':"departure_date", 'id':"departure_date"}))
    total_cost = forms.IntegerField(widget = forms.NumberInput(attrs ={'class':"form-control", 'type':'number','id':"total_cost"}))
    class Meta:
        
        fields = ('storage_type','no_of_units','description','arrival_date','departure_date','Total_cost')

           