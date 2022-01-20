from django import forms
from transport.models import Transport

class TransportForm(forms.ModelForm):
    class Meta:
        model = Transport
        fields = "__all__"