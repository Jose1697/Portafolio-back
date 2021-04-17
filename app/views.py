from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from app.models import *
from app.serializers import *
from django.contrib.auth.models import User
import jwt, datetime
# from app.models import Proyecto, ProyectoTecnologia, Recurso, Tecnologia, Usuario, UsuarioTecnologia
# from app.serializers import ProyectoSerializer, RecursoSerializer, TecnologiaSerializer
# Create your views here.


class RegisterView(APIView):
    def post(self,request):
        serializers = UserSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)

class LoginView(APIView):
    def post(self,request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()
        
        if user is None:
            raise AuthenticationFailed('User not found!')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload,'secret', algorithm='HS256').decode('utf-8')
        response = Response()
        response.set_cookie(key='jwt',value=token, httponly=True)
        response.data = {
            'jwt':token
        }

        return response

class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        
        try:
            payload = jwt.decode(token,'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)

class LogoutView(APIView):
    def post(self,request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message':'succes logout'
        }
        return response

class ProyectoList(generics.ListCreateAPIView):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

class ProyectoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer



class ProyectoTecnologiaList(generics.ListCreateAPIView):
    queryset = ProyectoTecnologia.objects.all()
    serializer_class = ProyectoTecnologiaSerializer

class ProyectoTecnologiaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProyectoTecnologia.objects.all()
    serializer_class = ProyectoTecnologiaSerializer




class RecursoList(generics.ListCreateAPIView):
    queryset = Recurso.objects.all()
    serializer_class = RecursoSerializer

class RecursoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recurso.objects.all()
    serializer_class = RecursoSerializer




class TecnologiaList(generics.ListCreateAPIView):
    queryset = Tecnologia.objects.all()
    serializer_class = TecnologiaSerializer

class TecnologiaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tecnologia.objects.all()
    serializer_class = TecnologiaSerializer



class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer



class UsuarioTecnologiaList(generics.ListCreateAPIView):
    queryset = UsuarioTecnologia.objects.all()
    serializer_class = UsuarioTecnologiaSerializer

class UsuarioTecnologiaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UsuarioTecnologia.objects.all()
    serializer_class = UsuarioTecnologiaSerializer




