from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Diseno, Servicio

@login_required
def agregar_diseno(request):
    servicios = Servicio.objects.filter(activo=True)
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        categoria = request.POST.get('categoria')
        precio = request.POST.get('precio')
        servicio_id = request.POST.get('servicio')
        imagen = request.FILES.get('imagen')
        descripcion = request.POST.get('descripcion', '')
        
        if not all([nombre, precio, servicio_id]):
            messages.error(request, '❌ Los campos nombre, precio y servicio son obligatorios')
            return redirect('agregar_diseno')
        
        diseno = Diseno(
            nombre=nombre,
            categoria=categoria,
            precio=precio,
            servicio_id=servicio_id,
            imagen=imagen,
            descripcion=descripcion,
            activo=True
        )
        diseno.save()
        messages.success(request, f'✅ Diseño "{nombre}" agregado correctamente')
        return redirect('dashboard')
    
    return render(request, 'core/agregar_diseno.html', {'servicios': servicios})
