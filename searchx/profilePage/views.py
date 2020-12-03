from home.models import History, Resultsave, Search
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from user.models import *

# Create your views here.
def serachhist(request):
    details = History.objects.filter(username=request.user)
    return render(request, 'profilePage/profile.html', locals())


'''
def favorites(request):
    new = Resultsave.objects.filter(username=request.user)
    print(new)
    return render(request,'profilePage/profile.html',locals())
'''


def favorites(request):
    new = Resultsave.objects.filter(username=request.user)
    return render(request, 'profilePage/profile.html', locals())

@login_required(login_url='/login')
def profile (request):
    #return HttpResponse('test')
    search = Search.objects.all()
    details = History.objects.filter(username=request.user)
    new = Resultsave.objects.filter(username=request.user)

    context = {
        'search':search,
        'details': details,
        'new': new,

        }
    return render(request, 'profilePage/profile.html', context)