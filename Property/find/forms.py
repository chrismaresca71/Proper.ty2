from django.forms import ModelForm
from .models import *

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
        exclude = ('agent',)

class HomeForm(ModelForm):
    class Meta:
        model = Home
        fields = '__all__'
        exclude = ('address','current_date')