from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import LoginForm, TaskForm, RegistrationForm
from .models import Task




class TaskView(ListView):
    model = Task
    template_name = 'home.html'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'details.html'


class TaskEditView(UpdateView):
    model = Task
    template_name = 'edit.html'
    fields = '__all__'

    def form_valid(self, form):
        task = form.save()
        return redirect('task_mngr_app:details', pk=task.pk)


# class TaskAddView(CreateView):
#    model = Task
#    template_name = 'add.html'
#    fields = '__all__'


# def form_valid(self, form):
#    task = form.save()
#    return redirect('task_mngr_app:details', pk=task.pk)


def task_add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task=form.save()
            return redirect('task_mngr_app:details', pk=task.pk)
    else:
        form = TaskForm()

    return render(request, 'add.html', {'form': form})


def user_login(request):
    loginError = False
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
            else:
                loginError = True
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form, 'loginError': loginError})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Po udanej rejestracji możesz przekierować użytkownika na inną stronę np. do strony logowania
            return redirect('login')  # Tutaj zastąp 'login' nazwą URL do strony logowania
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})