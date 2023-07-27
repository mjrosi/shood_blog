from django import forms
from crispy_forms.helper import FormHelper
from datetime import datetime
from phonenumber_field.formfields import PhoneNumberField
from .models import Booking

# The booking form users will use to book a delivery service


class BookingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    delivery_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date', 'min': datetime.now().date()}))

    phone = PhoneNumberField(widget=forms.TextInput(
        attrs={'placeholder': ('+353123456789')}))

    class Meta:
        model = Booking
        fields = (
            'name',
            'phone',
            'email',
            'delivery_date',
            'service',)
