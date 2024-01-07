from django.urls import path
from . import views
from .views import TaskView, TaskDetailView, TaskAddView, TaskEditView

urlpatterns = [
    path('', TaskView.as_view(), name="home"),
    path('details/<int:pk>', TaskDetailView.as_view(), name="details"),
    path('edit/<int:pk>', TaskEditView.as_view(), name='edit'),
    path('add/', TaskAddView.as_view(), name='add'),
]
