from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated 
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework import authentication
from django.contrib.auth.models import User
from django.contrib.auth import logout ,authenticate
from django.contrib.auth.hashers import make_password 
from rest_framework.authtoken.models import Token
from django.utils.timezone import now
import json 
from django.core.exceptions import ObjectDoesNotExist

#########################################
from apps.users.serializers import *
from apps.users.models import *

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        # Recuperamos las credenciales y autenticamos al usuario
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response({'response': 'Please provide both username and password'}, status=HTTP_400_BAD_REQUEST)
        try:
            userLog = User.objects.get(Q(username=username) | Q(email=username) )
            user = authenticate(username=userLog.username, password=password)
            serializer = UserSerializer(userLog)
            if not user:
                return Response({'response': 'Error Authentication '}, status=HTTP_404_NOT_FOUND)
            token, _ = Token.objects.get_or_create(user=user)
            userLog.last_login = now()
            userLog.save()
            return Response({'token': token.key, 'user': serializer.data},status=HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'response': 'Por favor ingrese Usuario/Email valido'}, status=HTTP_400_BAD_REQUEST)   
      

class LogoutView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    def post(self, request):        
        request.user.auth_token.delete()
        # Borramos de la request la información de sesión
        logout(request)
        # Devolvemos la respuesta al cliente
        return Response({'message':'Sessión Cerrada y Token Eliminado !!!!'},status=HTTP_200_OK)

class UserRegister(APIView):
    permission_classes = (AllowAny,)
    def post(self,request):
        data = json.loads(json.dumps(request.data))
        try:
            try:
                current_user = User.objects.get(username = data['username'])
                return Response({"response" : "El usuario ya existe"}, status=HTTP_400_BAD_REQUEST)
            except ObjectDoesNotExist:
                try:
                    current_user = User.objects.get(email = data['email'])
                    return Response({"response" : "El correo se encuentra en uso"}, status=HTTP_400_BAD_REQUEST)
                except ObjectDoesNotExist:
                    data['password'] = make_password(data['password'])
                    serializer = UserSerializerRegister(data=data)			
                    if serializer.is_valid():
                        serializer.save()					
                        validatedData = serializer.validated_data
                        try:
                            userid = User.objects.get(username = validatedData.get('username')).pk 
                            perfil = Profile(user_id = userid, phone= data['phone'] )
                            perfil.save()
                        except ObjectDoesNotExist:
                            return Response({"response" : "Usuario registrado pero con errores en perfil"},status=HTTP_200_OK)
                        return Response({"response" : "Usuario registrado"},status=HTTP_200_OK)
                        
                    return Response({"response" : serializer.errors}, status=HTTP_400_BAD_REQUEST)
        except KeyError :
            return Response({"response" : "Usuario Guardado Exitosamente!!!"}, status=HTTP_200_OK)
        
class ProfileView(APIView):
    queryset = Profile.objects.none()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        user = request.user
        profile = Profile.objects.get(user=user)
        serializer = self.serializer_class(profile)
        return Response(serializer.data)