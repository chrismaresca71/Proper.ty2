from django.urls import path
from find import views

urlpatterns = [
    path('', views.dashboard, name='agent-dashboard'),
    path('display-mode/', views.my_listings, name='display-mode'),
    path('create-listing/', views.create_listing, name='create-listing'),
    path('update-listing/<str:pk>/', views.update_listing, name='update-listing'),
    path('view/<str:pk>/', views.view_listing, name='view-listing'),
    path('delete/<str:pk>/', views.delete_listing, name='delete-listing'),


]