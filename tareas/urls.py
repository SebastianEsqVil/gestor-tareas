from django.urls import path
from . import views

urlpatterns = [
    path('', views.tablero, name='tablero'),
    path('crear/', views.crear_tarea, name='crear_tarea'),
    path('cambiar-estado/<int:tarea_id>/', views.cambiar_estado, name='cambiar_estado'),
]
