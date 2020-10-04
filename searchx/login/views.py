from django.shortcuts import HttpResponse, render
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def login(request):
    context = {}
    return render(request, 'login/loginpage.html', context)