from django.db import models 
import datetime
from users.models import *


class TypePost(BaseModel):
    """Define el tipo de publicacion (Alquiler, Venta de embarcaciones) o publicaciones de otros productos y servicios"""
    name = models.CharField(verbose_name='Tipo de publicacion', max_length=100) 
    description = models.TextField(verbose_name='Description', max_length=255,  blank=True)
    def __str__(self):
        return self.name
    
class Modality(BaseModel):
    """Define la modalidad del precio del servicio(hora, dia, semana o por persona)"""
    name = models.CharField(verbose_name='Modalidad', max_length=100) 
    description = models.TextField(verbose_name='Description', max_length=255,  blank=True)
    def __str__(self):
        return self.name
    
class Category(BaseModel):
    """Define la categoria de la embarcacion(Yate, lancha, jet sky)"""
    name = models.CharField(verbose_name='Categoria', max_length=100) 
    description = models.TextField(verbose_name='Description', max_length=255,  blank=True)
    def __str__(self):
        return self.name
    
class Features(BaseModel):
    """Define las accesorios de una embarcacion"""
    name = models.CharField(verbose_name='Caracteristicas', max_length=100) 
    description = models.TextField(verbose_name='Description', max_length=255,  blank=True)
    def __str__(self):
        return self.name
    
class Experiences(BaseModel):
    """Define el tipo de actividades que ofrece el servicio""" 
    name = models.CharField(verbose_name='Experiencia', max_length=100)
    description = models.TextField(verbose_name='Description', max_length=255,  blank=True)
    def __str__(self):
        return self.name
    
class ImagesPost(BaseModel): 
    url = models.URLField()

class Boat(BaseModel):
    """Descripcion de la Embarcacion""" 
    patent = models.CharField(max_length=50)
    capacity = models.IntegerField(default=0, verbose_name='Capacidad de Pasajeros')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(verbose_name='Nombre', max_length=100)
    description = models.TextField(verbose_name='Description', max_length=255,  blank=True)
    def __str__(self):
        return self.name

class Publication(BaseModel):
    title = models.CharField(max_length=100)
    descripcion = models.TextField(verbose_name='Descripcion',blank=True, null=True)
    #Addres = models.ForeignKey()"se refiere al punto de zarpe o marina
    #address = models.ForeignKey
    type_post = models.ForeignKey(TypePost, on_delete=models.PROTECT)
    modality = models.ForeignKey(Modality, on_delete=models.PROTECT)
    experiences = models.ForeignKey(Experiences, on_delete=models.PROTECT)    
    date_posted = models.DateTimeField(default=datetime.datetime.now, verbose_name='Fecha de Publicación')
    date_update = models.Choices
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Propietario')
    postImage = models.ImageField(null=True, blank=True, upload_to='imagesPublication/')
    is_published = models.BooleanField(default=False, verbose_name='Publicado?')
    status = models.BooleanField(default=False)
    moderator = models.ForeignKey('user.User', on_delete=models.PROTECT, verbose_name='Moderador')
    boat = models.ForeignKey(Boat, on_delete=models.PROTECT, verbose_name='Embarcacion')
    def __str__(self):
        return f'{self.pk}, {self.owner}, {self.date_posted}'
