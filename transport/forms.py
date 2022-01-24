from django import forms
from transport.models import Transport
from django.utils.translation import gettext_lazy as _

from units.models import Goods

class TransportForm(forms.ModelForm):
    address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id':"addressAutocomplete"}))

    class Meta:
        model = Transport
        exclude= ['user']
        labels = {
            'transport_type': _('Type of Transport'),
        }
        help_texts = {

        }
        widgets = {
            'transport_type': forms.RadioSelect(attrs={'class': "form-check-input"}),
        }
    # def __init__(self, user, *args, **kwargs):
    #     """ Grants access to the request object so that only goods of the current user
    #     are given as options"""
    #     super(TransportForm, self).__init__(*args, **kwargs)
        # self.fields['transport_goods'] = forms.ModelMultipleChoiceField(
        #     queryset = Goods.objects.filter(owner__id=user.id).all(),
        #     widget=forms.CheckboxSelectMultiple,
        # )
        
