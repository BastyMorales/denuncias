from django.db import models
from django.forms import ModelForm, TextInput, Textarea
import datetime

from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["titulo", "contenido"]
        widgets = {
            "titulo": TextInput(attrs={"class": "form-control"}),
            "contenido": Textarea(attrs={"class": "form-control"}),
        }


class Usuario(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Report(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  location = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class ReportImage(models.Model):
    report = models.ForeignKey(Report, on_delete=models.PROTECT)
    image_path = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    name = models.CharField(max_length=255)

class ReportCategory(models.Model):
    report = models.ForeignKey(Report, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

class ReportComment(models.Model):
    report = models.ForeignKey(Report, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Geolocation(models.Model):
    report = models.ForeignKey(Report, on_delete=models.PROTECT)
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

categorias = [
    [0, "Lugar de explotación"],
    [1, "Uso y/o contaminación de recursos naturales"],
    [2, "Residuos, emisiones e inmisiones"]
]

estados = [
    [0, "En revisión"],
    [1, "En procedimiento"],
    [2, "Finalizada"],
]
class RegistroDenuncia(models.Model):
    titulo = models.CharField(max_length=60, verbose_name= 'Ingrese titulo de denuncia')
    causa = models.IntegerField(choices=categorias, verbose_name='Causa de conflicto')
    asunto = models.TextField(max_length=200, verbose_name='Ingrese asunto')
    fecha_suceso = models.DateField(null=True, blank=True)
    hora_suceso = models.TimeField(null=True, blank=True)
    imagen = models.ImageField(upload_to='imagenes/', default='default.jpg')
    fecha_envio = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de ingreso')
    consentimiento = models.BooleanField(default=False)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    username = models.ForeignKey(User, on_delete=models.PROTECT, default=1)
    estado = models.IntegerField(choices=estados, verbose_name='Estado de la denuncia', default=0)


    def __str__(self) -> str:
        return self.titulo