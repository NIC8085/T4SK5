from django.urls import path
from . import views
from .views import TaskView

urlpatterns = [
    #path('', views.home, name="home"),
    path('', TaskView.as_view(), name="task")
]
