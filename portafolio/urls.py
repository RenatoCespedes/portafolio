"""portafolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, logout_then_login,LogoutView
from django.contrib.auth.decorators import login_required
from users.views import RegisterView, Profile,Mylogin 
from proyectos.views import Home,RegisterProject
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home.as_view(),name="home"),
    path('login/', Mylogin.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('profile/<str:usuario>',Profile.as_view(),name='profile'),
    path('registerProject/',RegisterProject.as_view(),name='new project')
]
