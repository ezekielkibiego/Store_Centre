from django import forms
from transport.models import Transport
from django.utils.translation import gettext_lazy as _

from units.models import Goods

class TransportForm(forms.ModelForm):
    address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id':"addressAutocomplete"}))

    class Meta:
        model = Transport
        fields= ['transport_type','address','phone_number']
        # labels = {
        #     'transport_type': _('Type of Transport'),
        # }
        # help_texts = {

        # }
        widgets = {
            'transport_type': forms.RadioSelect(attrs={'class': "form-check-input"}),
        }
        
