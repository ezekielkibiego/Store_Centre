from django import forms
from transport.models import Transport
from django.utils.translation import gettext_lazy as _

from units.models import Goods

class TransportForm(forms.ModelForm):
    address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id':"addressAutocomplete"}))

    class Meta:
        model = Transport
        fields= ['address','email','phone_number']
        labels = {
            'address': 'ADDRESS',
        }
        help_texts = {

        }
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Input your email'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Input phone number'})
        }
        error_messages={
            'phoneNumberRegex': _('Use the required formart +254712345678')
        }