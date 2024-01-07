from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Task


# def home(request):
#    return render(request, 'home.html', {})


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


class TaskAddView(CreateView):
    model = Task
    template_name = 'add.html'
    fields = '__all__'

    def form_valid(self, form):
        task = form.save()
        return redirect('task_mngr_app:details', pk=task.pk)