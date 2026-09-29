from django.contrib import admin
from .models import Categoria, Tarea, Comentario

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'color')

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'estado', 'prioridad', 'asignado_a', 'fecha_limite')
    list_filter = ('estado', 'prioridad', 'categoria')
    search_fields = ('titulo', 'descripcion')

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('tarea', 'autor', 'creado_en')
