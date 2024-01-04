from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Task


# def home(request):
#    return render(request, 'home.html', {})


class TaskView(ListView):
    model = Task
    template_name = 'home.html'
