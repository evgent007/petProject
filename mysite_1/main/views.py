from django.shortcuts import render
from .models import Task
from django.http import HttpResponse

def index1(request):

    return render(request, 'main/index1.html', )

def elena(request):
    tasks = Task.objects.order_by('task')
    return render(request, 'main/elena.html', {'tasks': tasks})

def about(request):
    return render(request, 'main/about.html')

def registration(request):
    return render(request, 'main/regist.html')


# Create your views here.
