from django.shortcuts import HttpResponse, render
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    # form = UserCreationForm()
    # context = {'form': form}
    return render(request, 'register/register.html')