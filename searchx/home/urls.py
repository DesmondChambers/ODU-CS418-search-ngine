from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path(r'^favorite_add/(?P<str:title>\w+)/$', views.favorite_add,name='favorite_add'),
]