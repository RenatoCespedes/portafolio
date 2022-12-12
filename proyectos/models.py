from django.db import models
from django.db.models.fields import CharField,URLField,EmailField,TextField
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User
# Create your models here.
class ProjectModel(models.Model):
    foto= ImageField(upload_to="images/")
    titulo=CharField(max_length=100)
    descripcion=CharField(max_length=1000)
    tags=CharField(max_length=500)
    repo_url=URLField(blank=True)
    usuarios=models.ForeignKey(User,on_delete=models.CASCADE)