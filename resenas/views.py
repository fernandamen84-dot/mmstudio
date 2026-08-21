from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Resena

def agregar_resena(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        calificacion = request.POST.get('calificacion')
        comentario = request.POST.get('comentario')
        foto = request.FILES.get('foto')
        
        if not all([nombre, calificacion, comentario]):
            messages.error(request, '❌ Por favor llena todos los campos requeridos.')
            return redirect('agregar_resena')
        
        resena = Resena(
            nombre=nombre,
            calificacion=calificacion,
            comentario=comentario,
            foto=foto,
            aprobada=False
        )
        resena.save()
        
        messages.success(request, '⭐ ¡Gracias por tu reseña! La revisaremos y la publicaremos pronto. 💕')
        return redirect('home')
    
    return render(request, 'resenas/agregar.html')


def ver_resenas(request):
    resenas = Resena.objects.filter(aprobada=True)
    return render(request, 'resenas/lista.html', {
        'resenas': resenas
    })


# ========== FUNCIONES PARA EL DASHBOARD ==========

@login_required
def gestionar_resenas(request):
    """Vista para gestionar todas las reseñas desde el dashboard"""
    resenas_pendientes = Resena.objects.filter(aprobada=False)
    resenas_aprobadas = Resena.objects.filter(aprobada=True)
    
    context = {
        'resenas_pendientes': resenas_pendientes,
        'resenas_aprobadas': resenas_aprobadas,
    }
    return render(request, 'core/gestionar_resenas.html', context)


@login_required
def aprobar_resena(request, resena_id):
    """Aprobar una reseña para que sea visible en la página"""
    resena = get_object_or_404(Resena, id=resena_id)
    resena.aprobada = True
    resena.save()
    messages.success(request, f'✅ Reseña de {resena.nombre} APROBADA correctamente ✅')
    return redirect('gestionar_resenas')


@login_required
def eliminar_resena(request, resena_id):
    """Eliminar una reseña (permanentemente)"""
    resena = get_object_or_404(Resena, id=resena_id)
    nombre = resena.nombre
    resena.delete()
    messages.success(request, f'🗑️ Reseña de {nombre} ELIMINADA 🗑️')
    return redirect('gestionar_resenas')
