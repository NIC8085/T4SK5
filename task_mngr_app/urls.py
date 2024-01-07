from django.urls import path
from . import views
from .views import TaskView, TaskDetailView, TaskEditView

app_name = 'task_mngr_app'

urlpatterns = [
    path('', TaskView.as_view(), name="home"),
    path('details/<int:pk>', TaskDetailView.as_view(), name="details"),
    path('edit/<int:pk>', TaskEditView.as_view(), name='edit'),
    path('add/', views.task_add, name='add'),
    path('login/', views.user_login, name='login'),
]
