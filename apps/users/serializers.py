from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import *

class UserSerializer(serializers.ModelSerializer):
    last_login = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = User
        fields = ('username','email', 'first_name','last_name','last_login','is_staff','is_active')
         #esconder password
        extra_kwargs = {
            'password': {'write_only': True, 'required': True}
        }

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

