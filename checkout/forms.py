from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number', 'street_address1', 'street_address2', 'town_or_city', 'county', 'country', 'postcode',)

    def __init__(*args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full name',
            'email': 'Email address',
            'phone_number': 'Phone number',
            'street_address1': 'Street address line 1',
            'street_address2': 'Street address line 2',
            'town_or_city': 'Town or city',
            'county': 'County',
            'country': 'Country',
            'postcode': 'Postcode',
        }

