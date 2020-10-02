from django.shortcuts import HttpResponse, render

# Create your views here.

def register(request):
    # return HttpResponse('register')
    return render(request, 'register/register.html')