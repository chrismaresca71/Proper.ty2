from django.urls import path
from registration import views

urlpatterns = [
    path('register/', views.Register, name='agents-register'),
    path('login/', views.LoginAgent, name='agents-login'),
    path('logout/', views.LogoutAgent, name='agents-logout')
]