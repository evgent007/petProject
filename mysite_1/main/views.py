from django.shortcuts import render
from django.http import HttpResponse

def index1(request):
    return render(request, 'main/index1.html')

def elena(request):
    return render(request, 'main/elena.html')


# Create your views here.
