from django.db import models
from django.db.models.fields import CharField,URLField,EmailField,TextField
from django.db.models.fields.files import ImageField
# Create your models here.
class Contacto(models.Model):
    nombre=CharField(max_length=50)
    correo=EmailField()
    tema=CharField(max_length=100)
    mensaje=TextField()