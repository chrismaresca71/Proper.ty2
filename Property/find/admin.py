from django.contrib import admin
from .models import *

registered = [Address, Home]

admin.site.register(registered)