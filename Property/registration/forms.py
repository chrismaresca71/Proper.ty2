from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class AgentForm(forms.ModelForm):
    company = forms.CharField()
    location = forms.CharField()
    profile_picture = forms.ImageField()

    class Meta:
        model = Agent
        fields = ('company', 'location','profile_picture')


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2', 'is_agent', 'is_client']

    

    

