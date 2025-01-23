from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone number',
            'default_postcode': 'Postcode',
            'default_town_or_city': 'Town or city',
            'default_street_address1': 'Street address line 1',
            'default_street_address2': 'Street address line 2',
            'default_county': 'County, state or municipality',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs[
                'class'
            ] = 'border-black rounded-0 profile-form-input'

            self.fields[field].label = False
