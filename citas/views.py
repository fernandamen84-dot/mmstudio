from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Cita
from catalogo.models import Servicio, Diseno

def agendar_cita(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        telefono = request.POST.get('telefono')
        instagram = request.POST.get('instagram', '')
        servicio_id = request.POST.get('servicio')
        diseno_id = request.POST.get('diseno')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        notas = request.POST.get('notas', '')
        
        # Validar que todos los campos requeridos estén llenos
        if not all([nombre, telefono, servicio_id, fecha, hora]):
            messages.error(request, '❌ Por favor llena todos los campos requeridos.')
            return redirect('agendar')
        
        # Crear la cita
        cita = Cita(
            nombre=nombre,
            telefono=telefono,
            instagram=instagram,
            servicio_id=servicio_id,
            diseno_id=diseno_id if diseno_id else None,
            fecha=fecha,
            hora=hora,
            notas=notas
        )
        cita.save()
        
        # Mensaje de éxito
        messages.success(request, f'✨ ¡Cita agendada con éxito! Te esperamos el {fecha} a las {hora}. Te enviaremos confirmación por WhatsApp 💕')
        
        # Redirigir a la página de agendar pero con mensaje
        return redirect('agendar')
    
    # GET - Mostrar el formulario
    servicios = Servicio.objects.filter(activo=True)
    disenos = Diseno.objects.filter(activo=True)
    
    return render(request, 'citas/agendar.html', {
        'servicios': servicios,
        'disenos': disenos,
    })


# ========== FUNCIONES PARA EL DASHBOARD ==========

@login_required
def gestionar_citas(request):
    """Vista para gestionar todas las citas desde el dashboard"""
    citas_pendientes = Cita.objects.filter(estado='pendiente')
    citas_confirmadas = Cita.objects.filter(estado='confirmada')
    citas_completadas = Cita.objects.filter(estado='completada')
    citas_canceladas = Cita.objects.filter(estado='cancelada')
    
    context = {
        'citas_pendientes': citas_pendientes,
        'citas_confirmadas': citas_confirmadas,
        'citas_completadas': citas_completadas,
        'citas_canceladas': citas_canceladas,
    }
    return render(request, 'core/gestionar_citas.html', context)


@login_required
def cambiar_estado_cita(request, cita_id, estado):
    """Cambiar el estado de una cita (confirmar, cancelar, completar)"""
    cita = get_object_or_404(Cita, id=cita_id)
    
    # Validar que el estado sea válido
    estados_validos = ['confirmada', 'cancelada', 'completada']
    if estado not in estados_validos:
        messages.error(request, '❌ Estado no válido.')
        return redirect('gestionar_citas')
    
    # Guardar el estado anterior para el mensaje
    estado_anterior = cita.get_estado_display()
    cita.estado = estado
    cita.save()
    
    # Mensaje según el estado
    if estado == 'confirmada':
        messages.success(request, f'✅ Cita de {cita.nombre} CONFIRMADA ✅')
    elif estado == 'cancelada':
        messages.success(request, f'❌ Cita de {cita.nombre} CANCELADA ❌')
    elif estado == 'completada':
        messages.success(request, f'💅 Cita de {cita.nombre} COMPLETADA 💅')
    
    return redirect('gestionar_citas')
