from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Tarea, Categoria

def tablero(request):
    tareas_pendientes = Tarea.objects.filter(estado=Tarea.Estado.PENDIENTE).select_related('categoria', 'asignado_a')
    tareas_progreso = Tarea.objects.filter(estado=Tarea.Estado.EN_PROGRESO).select_related('categoria', 'asignado_a')
    tareas_completadas = Tarea.objects.filter(estado=Tarea.Estado.COMPLETADA).select_related('categoria', 'asignado_a')
    categorias = Categoria.objects.all()

    context = {
        'pendientes': tareas_pendientes,
        'progreso': tareas_progreso,
        'completadas': tareas_completadas,
        'categorias': categorias,
        'total_tareas': Tarea.objects.count(),
        'total_completadas': tareas_completadas.count(),
    }
    return render(request, 'tareas/tablero.html', context)

@require_POST
def cambiar_estado(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    nuevo_estado = request.POST.get('nuevo_estado')
    if nuevo_estado in Tarea.Estado.values:
        tarea.estado = nuevo_estado
        tarea.save()
    return redirect('tablero')

@require_POST
def crear_tarea(request):
    titulo = request.POST.get('titulo')
    descripcion = request.POST.get('descripcion', '')
    prioridad = request.POST.get('prioridad', Tarea.Prioridad.MEDIA)
    categoria_id = request.POST.get('categoria')

    categoria = None
    if categoria_id:
        categoria = Categoria.objects.filter(id=categoria_id).first()

    if titulo:
        Tarea.objects.create(
            titulo=titulo,
            descripcion=descripcion,
            prioridad=prioridad,
            categoria=categoria,
            asignado_a=request.user if request.user.is_authenticated else None
        )
    return redirect('tablero')
