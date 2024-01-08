from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class State(models.Model):
    title = models.CharField(max_length=50, null=True, default=None)
    weight = models.IntegerField(default=0, validators=[MaxValueValidator(2), MinValueValidator(0)])
    color = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    working_person = models.CharField(max_length=30)
    creation_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    deadline = models.DateTimeField()
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    files = models.FileField(upload_to='task_files/', null=True, blank=True)

    def __str__(self):
        return self.title
