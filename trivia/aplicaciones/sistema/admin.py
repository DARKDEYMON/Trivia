from django.contrib import admin
from trivia.aplicaciones.sistema.models import *
from trivia.aplicaciones.sistema.forms import *
# Register your models here.
class form_usuario_admin(admin.ModelAdmin):
    form = form_usuario_for_admin
    search_fields = ('username','correo',)
    list_display = ('username','correo',)
admin.site.register(usuario,form_usuario_admin)