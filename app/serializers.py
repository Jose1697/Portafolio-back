from rest_framework import serializers
from app.models import Proyecto, ProyectoTecnologia, Recurso, Tecnologia, Usuario, UsuarioTecnologia

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = ('idproyectos','nombre','idusuario')

class RecursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recurso
        fields = ('idrecurso','nombre','imagen','descripcion','idproyectos')


class TecnologiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnologia
        fields = ('idtecnologia','nombre','imagen')