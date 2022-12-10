from django import forms
from django.contrib.auth.forms import UserCreationForm


class ProjectForm(forms.Form):
    foto= forms.CharField(max_length=800)
    titulo=forms.CharField(max_length=100)
    descripcion=forms.CharField(max_length=1000)
    tags=forms.CharField(max_length=500)
    repo_url=forms.CharField(max_length=800)