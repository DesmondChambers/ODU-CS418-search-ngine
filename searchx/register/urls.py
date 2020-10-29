from django.urls import path 
from django.conf.urls import url
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('activate/<uidb64>/<token>/',views.activate, name='activate'), 
]