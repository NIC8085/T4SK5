from django import forms
from django.contrib.auth.models import User

from .models import State, Task


class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = ['title', 'weight', 'color']


class TaskForm(forms.ModelForm):
    delete_files = forms.BooleanField(required=False, initial=False, label='Delete Files')

    class Meta:
        model = Task
        fields = ['title', 'working_person', 'start_date', 'end_date', 'deadline', 'state', 'content', 'files']

        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'placeholder': 'Enter username'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput(attrs={'placeholder': 'Repeat password'}))

    class Meta:
        model = User
        fields = ['username']

    def clean_password2(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords don't match.")

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user