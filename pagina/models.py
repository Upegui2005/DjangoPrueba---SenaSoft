from django.db import models


# Create your models here.


class Usuarios(models.Model):
    idUsuario = models.BigIntegerField(primary_key=True, blank=True)
    email = models.EmailField(unique=True)
    contrasella = models.CharField(max_length=100)
    fechaRegistro = models.DateField(auto_now_add=True)
    nombre = models.CharField(max_length=100)


class Comunidades(models.Model):
    idComunidad = models.BigAutoField(primary_key=True, blank=True)
    nombreComunidad = models.CharField(max_length=255, unique=True)
    descripcion = models.CharField(max_length=255)


class Publicaciones(models.Model):
    idPublicacion = models.BigAutoField(primary_key=True, blank=True)
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    idUsuario = models.ForeignKey('Usuarios', on_delete=models.CASCADE, null=True)
    idComunidad = models.ForeignKey('Comunidades', on_delete=models.CASCADE, null=True)


class Comentarios(models.Model):
    idComentario = models.BigAutoField(primary_key=True, blank=True)
    contenido = models.CharField(max_length=150)
    idUsuario = models.ForeignKey('Usuarios', on_delete=models.CASCADE, null=True)
    idPublicacion = models.ForeignKey('Publicaciones', on_delete=models.CASCADE, null=True)


class UsuarioComunidad(models.Model):
    idUsuarioComunidad = models.BigAutoField(primary_key=True, blank=True)
    idUsuario = models.ForeignKey('Usuarios', on_delete=models.CASCADE, null=True)
    idComunidad = models.ForeignKey('Comunidades', on_delete=models.CASCADE, null=True)
