from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import CreateView
from projectForm.form import ProjectForm, NewUserForm,ContactForm
from django.contrib.auth.decorators import login_required
from .models import ProjectModel,Contacto
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from django.urls import reverse
# Create your views here.


class RegisterProject(LoginRequiredMixin,View):
    login_url = '/login/'
    redirect_field_name = '/registroProjecto/'
    template='registroProjecto.html'
    context={}
    context["form"] = ProjectForm()
    def get(self,request):
        return render(request,self.template,self.context)
    def post(self,request):
        form= ProjectForm(request.POST)
        
        if form.is_valid():
            project = ProjectModel.objects.create(foto=form.cleaned_data['foto'],
            titulo=form.cleaned_data['titulo'],descripcion=form.cleaned_data['descripcion'],
            tags=form.cleaned_data['tags'],repo_url=form.cleaned_data['repo_url'])
            return redirect('home')