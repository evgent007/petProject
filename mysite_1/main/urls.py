

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index1, name='glav'),
    path('elena', views.elena, name='elena'),
    path('about', views.about, name='about'),
    path('registration', views.registration, name='regist')
]