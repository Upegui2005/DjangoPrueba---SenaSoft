from django.contrib import admin

from pagina.models import Comentarios, Comunidades, Publicaciones, UsuarioComunidad, Usuarios


# Register your models here.


class UsuariosAdmin(admin.ModelAdmin):
    fields = ["email", "contrasella", "nombre"]
    list_display = ["idUsuario", "email", "contrasella", "fechaRegistro", "nombre"]


class ComunidadesAdmin(admin.ModelAdmin):
    fields = ["nombreComunidad", "descripcion"]
    list_display = ["idComunidad", "nombreComunidad", "descripcion"]


class PublicacionesAdmin(admin.ModelAdmin):
    fields = ["titulo", "contenido", "idUsuario", "idComunidad"]
    list_display = ["idPublicacion", "titulo", "contenido", "idUsuario", "idComunidad"]


class ComentariosAdmin(admin.ModelAdmin):
    fields = ["contenido", "idUsuario", "idPublicacion"]
    list_display = ["idComentario", "contenido", "idUsuario", "idPublicacion"]


class UsuariosComunidadAdmin(admin.ModelAdmin):
    fields = ["idUsuario", "idComunidad"]
    list_display = ["idUsuarioComunidad", "idUsuario", "idComunidad"]


admin.site.register(Usuarios, UsuariosAdmin)
admin.site.register(Comunidades, ComunidadesAdmin)
admin.site.register(Publicaciones, PublicacionesAdmin)
admin.site.register(Comentarios, ComentariosAdmin)
admin.site.register(UsuarioComunidad, UsuariosComunidadAdmin)
