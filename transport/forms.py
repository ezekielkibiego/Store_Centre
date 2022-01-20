from django import forms
from transport.models import Transport
from django.utils.translation import gettext_lazy as _

class TransportForm(forms.ModelForm):
    class Meta:
        model = Transport
        exclude= ['user',]
        labels = {
            'transport_type': _('Type of Transport'),
        }
        help_texts = {

        }
        widgets = {
            'transport_type': forms.RadioSelect(attrs={'class': "form-check-input"}),
        }