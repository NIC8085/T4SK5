from django.urls import path
from . import views
from .views import TaskView, TaskDetailView

urlpatterns = [
    #path('', views.home, name="home"),
    path('', TaskView.as_view(), name="task"),
    path('TaskDetail/<int:pk>', TaskDetailView.as_view(), name="task-detail"),
]
