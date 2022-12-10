from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import CreateView
from .form import ProjectForm
from django.contrib.auth.decorators import login_required
from .models import ProjectModel
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from django.urls import reverse


class ProjectList(ListView):
    model = ProjectModel
    template_name = "profile.html"
    data = ProjectModel.objects.all()    

class ElementProjecto(View):
    template='element.html'
    context={}
    def get(self,request,id,usuario):
        project=ProjectModel.objects.filter(id=id)
        self.context["project"]=project[0]
        return render(request,self.template,self.context)

class Editelement(View):
    template='edition.html'
    context={}
    def get(self,request,id,usuario):
        elem=ProjectModel.objects.filter(id=id)
        form=ProjectForm()
        self.context['form']=form
        self.context['elem']=elem[0]
        self.context['usuario']=usuario
        return render(request,self.template,self.context)
    def post(self,request,id,usuario):
        element=ProjectModel.objects.get(id=id)
        # element=elem[0]
        form_elem=ProjectForm(request.POST)
        print("-----------------------")
        print(form_elem.is_valid())
        print("-----------------------")
        if form_elem.is_valid():
            element.foto=form_elem.cleaned_data['foto']
            element.titulo=form_elem.cleaned_data['titulo']
            element.descripcion=form_elem.cleaned_data['descripcion']
            element.tags=form_elem.cleaned_data['tags']
            element.repo_url=form_elem.cleaned_data['repo_url']
            element.save()
            return redirect(reverse('element',kwargs={'id':id,'usuario':usuario}))
        return HttpResponse('No se llego a validar')

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
        
class Home(View):
    def get(self,request):
        return render(request, 'index.html', {})

def delete(request, id,usuario):
    data = ProjectModel.objects.get(id=id) 
    data.delete()
    # message.suc
    return redirect(reverse('profile',kwargs={'usuario':usuario}))