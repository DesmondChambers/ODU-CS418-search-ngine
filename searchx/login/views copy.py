from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages,auth
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.

def loginpage(request):
	if request.user.is_authenticated:
    		return redirect('/user')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				auth.login(request, user)
				return redirect('/user/user.html')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login/loginpage.html', context)

def logoutUser(request):
	logout(request)
	return redirect('/')