from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('exe_open', views.exe_open, name='exe_open'),
    path('exe_close', views.exe_close, name='exe_close'),
]