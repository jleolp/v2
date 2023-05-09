from rest_framework import routers
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
 
 

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('register/', UserRegister.as_view()),
    path('profile/', ProfileView.as_view()),
]  
