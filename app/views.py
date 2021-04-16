from django.shortcuts import render
from rest_framework import generics
from app.models import Proyecto, ProyectoTecnologia, Recurso, Tecnologia, Usuario, UsuarioTecnologia
from app.serializers import ProyectoSerializer, RecursoSerializer, TecnologiaSerializer
# Create your views here.
