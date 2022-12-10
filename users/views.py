from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import CreateView
from .form import NewUserForm,ContactForm
from proyectos.form import ProjectForm
from django.contrib.auth.decorators import login_required
from .models import ProjectModel,Contacto
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
# Create your views here.
class RegisterView(CreateView):
  template_name = "registration/register.html"
  form_class = NewUserForm

  def form_valid(self, form):
      form.save()
      return redirect('login')


class Profile(View):
    template='profile.html'
    model = ProjectModel
    data = ProjectModel.objects.all() 
    context={}
    def get(self,request,usuario):
        form=ProjectForm()
        form1=ContactForm()
        self.context['form']=form
        self.context['form1']=form1
        self.context['usuario']=usuario
        self.context['data']=self.data
        return render(request,self.template, self.context)
    def post(self,request,usuario):
        form= ProjectForm(request.POST)
        form1=ContactForm(request.POST)


        # if not form1:
        if  form.is_valid():
                project = ProjectModel.objects.create(foto=form.cleaned_data['foto'],
                titulo=form.cleaned_data['titulo'],descripcion=form.cleaned_data['descripcion'],
                tags=form.cleaned_data['tags'],repo_url=form.cleaned_data['repo_url'])
                return redirect(reverse('profile',kwargs={'usuario':usuario}))
        # elif not form:
        if form1.is_valid():
                contacto=Contacto.objects.create(nombre=form1.cleaned_data['nombre'],
                correo=form1.cleaned_data['correo'],tema=form1.cleaned_data['tema'],mensaje=form1.cleaned_data['mensaje'])
                return redirect(reverse('profile',kwargs={'usuario':usuario}))


class Mylogin(View):
    template_name = "registration/login.html"
    template_post="registration/register.html"
    context={}
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('/profile')
        form = AuthenticationForm()
        self.context['form']=form
        return render(request,self.template_name,self.context)
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(f'/profile/{username}')
        else:
            form=AuthenticationForm()
            self.context['form']=form
            return render(request,self.template_post,self.context) 