from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import User, Profile, UserFleetingData, ChangePasswordList

# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ('id','username','email')
admin.site.register(User, CustomUserAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user','modified', 'image')
admin.site.register(Profile, ProfileAdmin)
