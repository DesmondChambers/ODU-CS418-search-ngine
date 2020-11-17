from django.shortcuts import HttpResponse, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserResgisterForm
from django.shortcuts import render, redirect
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
#from validate-email import validate_email
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
#from .utils import account_activation_token
from django.urls import reverse
from django.contrib import auth
from searchx import settings
import json
import urllib
# Create your views here.


def register (request):
    if request.method == 'POST':
        form = UserResgisterForm(request.POST)
        if form.is_valid():
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
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account created for {username}')
                return redirect ('/user')
    else:
        form = UserResgisterForm()
    return render(request, 'register/register.html', {'form': form})