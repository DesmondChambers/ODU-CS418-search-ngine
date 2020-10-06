from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginpage, name='loginpage'),
    path('logout/', views.logoutUser, name='logout'),
]