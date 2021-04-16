from django.shortcuts import render
from rest_framework import generics
from app.models import *
from app.serializers import *
# from app.models import Proyecto, ProyectoTecnologia, Recurso, Tecnologia, Usuario, UsuarioTecnologia
# from app.serializers import ProyectoSerializer, RecursoSerializer, TecnologiaSerializer
# Create your views here.

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




