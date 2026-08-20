from django.shortcuts import render, redirect
from django.contrib import messages
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