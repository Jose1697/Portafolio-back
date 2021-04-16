from rest_framework import serializers
from app.models import Proyecto, ProyectoTecnologia, Recurso, Tecnologia, Usuario, UsuarioTecnologia

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = ('idproyectos','nombre','idusuario')





class ProyectoTecnologiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProyectoTecnologia
        fields = ('proyecto_idproyectos','tecnologia_idtecnologia')



class RecursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recurso
        fields = ('idrecurso','nombre','imagen','descripcion','idproyectos')





class TecnologiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnologia
        fields = ('idtecnologia','nombre','imagen')



class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('idusuario','descripcion','imagen','usuario')


class UsuarioTecnologiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioTecnologia
        fields = ('usuario_idusuario','tecnologia_idtecnologia')