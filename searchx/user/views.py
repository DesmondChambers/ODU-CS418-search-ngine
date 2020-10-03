from django.shortcuts import HttpResponse, render

# Create your views here.
def user (request):
    # return HttpResponse('home')
    return render(request, 'user/user.html')

def profile (request):
    #return HttpResponse('test')
    return render(request, 'user/profile.html')