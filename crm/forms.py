from django import forms
from .models import CustomerData


class AddRecordForm(forms.ModelForm):
    class Meta:
        model = CustomerData
        fields = ('first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'zipcode')
