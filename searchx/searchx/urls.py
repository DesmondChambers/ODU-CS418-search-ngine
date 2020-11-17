"""searchx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from profilePage.views import profile
from user.views import user
from register.views import register
from login.views import logoutUser, login, loginpage
from home.views import home
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    #path('', home),
    #path('login/', loginpage),
    #path('login/', include('login.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login/loginpage.html'), name='login'),
    path('logout/', logoutUser),
    #path('logout/', auth_views.LogoutView.as_view(), name='logoutUser'),
    path('register/', register),
    path('user/', user),
    path('profile/', profile),
    #path('profile/', include('profilePage.urls')),
]

# urlpatterns += staticfiles_urlpatterns(