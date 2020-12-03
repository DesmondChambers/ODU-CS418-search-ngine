from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages,auth
from django.contrib.auth import authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json
import urllib
from searchx import settings

# Create your views here.
def login(request):
    if request.method == 'POST':
        #Login User
        username = request.POST['username'] 
        password = request.POST['password'] 
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret' : settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req = urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        if result['success']:
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                messages.success(request,'You are now logged in')
                return redirect('/user/user.html')
            else:
                messages.error(request, 'Invalid Credentials')
                return redirect('/login')
        else:
            
            messages.error(request, 'Invalid reCAPTCHA, Please Try again')
            return redirect('/login')

    else:
        return render(request,'/login')



def logoutUser(request):
	logout(request)
	return redirect('/')