from django.shortcuts import HttpResponse, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserResgisterForm

# Create your views here.

def register (request):
    if request.method == 'POST':
        form = UserResgisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect ('/user')
    else:
        form = UserResgisterForm()
    return render(request, 'register/register.html', {'form': form})

