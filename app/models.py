
from django.db import models


class Proyecto(models.Model):
    idproyectos = models.IntegerField(db_column='idProyectos', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=100)
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='idUsuario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Proyecto'


class ProyectoTecnologia(models.Model):
    proyecto_idproyectos = models.OneToOneField(Proyecto, models.DO_NOTHING, db_column='Proyecto_idProyectos', primary_key=True)  # Field name made lowercase.
    tecnologia_idtecnologia = models.ForeignKey('Tecnologia', models.DO_NOTHING, db_column='Tecnologia_idTecnologia')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Proyecto_Tecnologia'
        unique_together = (('proyecto_idproyectos', 'tecnologia_idtecnologia'),)


class Recurso(models.Model):
    idrecurso = models.IntegerField(db_column='idRecurso', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45)
    imagen = models.CharField(max_length=1200, blank=True, null=True)
    descripcion = models.CharField(max_length=1200, blank=True, null=True)
    idproyectos = models.ForeignKey(Proyecto, models.DO_NOTHING, db_column='idProyectos')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Recurso'


class Tecnologia(models.Model):
    idtecnologia = models.IntegerField(db_column='idTecnologia', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45)
    imagen = models.CharField(max_length=1200)

    class Meta:
        managed = False
        db_table = 'Tecnologia'


class Usuario(models.Model):
    idusuario = models.IntegerField(db_column='idUsuario', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=1200, blank=True, null=True)
    imagen = models.CharField(max_length=1200)

    class Meta:
        managed = False
        db_table = 'Usuario'


class UsuarioTecnologia(models.Model):
    usuario_idusuario = models.OneToOneField(Usuario, models.DO_NOTHING, db_column='Usuario_idUsuario', primary_key=True)  # Field name made lowercase.
    tecnologia_idtecnologia = models.ForeignKey(Tecnologia, models.DO_NOTHING, db_column='Tecnologia_idTecnologia')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Usuario_Tecnologia'
        unique_together = (('usuario_idusuario', 'tecnologia_idtecnologia'),)
