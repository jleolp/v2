# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django .utils import timezone
from django.core.exceptions import ValidationError
from apps.tools.models import Countries, States, Cities

def unique_rand():
    while True:
        code = User.objects.make_random_password(length=24)
        return code

def week_day_hence():
    return timezone.now() + timezone.timedelta(days=7)

def hour_day_hence():
    return timezone.now() + timezone.timedelta(minutes=10)

def unique_devices_code():
    import secrets
    return secrets.token_hex(32).upper()

def unique_login_code():
    import secrets
    return secrets.token_hex(3).upper()

PLATFORM = (
    (0,'WEB'),  
    (1,'MOBILE')
)

class BaseModel(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True, editable=False)
    updatedAt = models.DateTimeField(auto_now=True)
    
class User(AbstractUser):
    def __str__(self):
        user_fullname = self.first_name+' '+self.last_name
        return '%s' % (user_fullname)       
     
class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=255, unique=True,  null=True)
    dni = models.CharField(max_length=20, unique=True,verbose_name='Cedula de identidad', blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to='photo/')
    country = models.ForeignKey(Countries, verbose_name=("Pais"), on_delete=models.SET_NULL, null=True)
    state = models.ForeignKey(States, verbose_name=("Estado"), on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(Cities, verbose_name=("Ciudad"), on_delete=models.SET_NULL, null=True)
   
class ChangePasswordList(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=25, unique=True)
    finish = models.BooleanField(default=False)
    expires = models.DateTimeField(default=hour_day_hence)
    
    class Meta:
        db_table = str(__package__.split('.')[1])+'_request_change_password'
        verbose_name = 'Peticion cambio de password'

class UserDevicesLogin(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=64, default=unique_devices_code)
    fbm_token = models.CharField(max_length=250, blank=True, null=True) #Token de firebase massage
    platform = models.IntegerField(choices=PLATFORM,default=PLATFORM[1][0])
    platform_name = models.CharField(max_length=150)
    active = models.BooleanField(default=False)
    last_request = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = str(__package__.split('.')[1])+'_user_devices_login'
        verbose_name = 'Dispositivos de usuarios logeados'


class UserFleetingData(BaseModel):
    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    #user_type = models.ForeignKey(CompanyUsersType, on_delete=models.SET_NULL, null=True)
    specialties = models.TextField() # Se guarda una lista de ID para no generar otra tabla innecesaria
    code  = models.CharField(max_length=25 , unique=True)
    expires = models.DateTimeField(default=week_day_hence)

    def __str__(self):
        return '%s | %s ' % (self.username, self.email)

    class Meta:
        db_table = str(__package__.split('.')[1])+'_user_fleeting'
        verbose_name = 'Usuarios Temporal'
