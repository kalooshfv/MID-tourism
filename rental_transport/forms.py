from django import forms
from rental_transport.models import TransportList

class Transportlistform(forms.ModelForm):
    class Meta:
        model = TransportList
        fields = [
            "company_name",
            "transport_name",
            "transport_price",
            "description",
            "availability",
        ]