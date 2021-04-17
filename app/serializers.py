from rest_framework import serializers
from django.contrib.auth.models import User
from app.models import Proyecto, ProyectoTecnologia, Recurso, Tecnologia, Usuario, UsuarioTecnologia, AuthUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ( "id", "username", "password", "first_name", "last_name", "email")
        extra_kwargs = {
            'password':{'write_only': True}
        }
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


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