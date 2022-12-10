from django.db import models
from django.db.models.fields import CharField,URLField,EmailField,TextField
# Create your models here.
class ProjectModel(models.Model):
    foto= CharField(max_length=100)
    titulo=CharField(max_length=100)
    descripcion=CharField(max_length=1000)
    tags=CharField(max_length=500)
    repo_url=URLField(blank=True)