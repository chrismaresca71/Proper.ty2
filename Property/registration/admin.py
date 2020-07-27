#From Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

#From Project
from .models import *


#Import Models
myModels = [Client, Agent]
admin.site.register(myModels)

UserAdmin.fieldsets += ('Custom fields set', {'fields': ('is_agent', 'is_client')}),

admin.site.register(User, UserAdmin)




