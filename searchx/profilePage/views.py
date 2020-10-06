from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from user.models import *
from register.forms import UserResgisterForm

# Create your views here.

@login_required(login_url='/login')
def profile (request):
    #return HttpResponse('test')
    return render(request, 'profilePage/profile.html')