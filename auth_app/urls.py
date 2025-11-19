# auth_app/urls.py
from django.urls import path
from . import views

app_name = 'auth_app'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/delete/', views.delete_account, name='delete_account'),
]