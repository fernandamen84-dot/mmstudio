from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from catalogo.models import Diseno, Servicio
from citas.models import Cita
from resenas.models import Resena
from datetime import date

def home(request):
    disenos = Diseno.objects.filter(activo=True)[:6]
    servicios = Servicio.objects.filter(activo=True)
    resenas = Resena.objects.filter(aprobada=True)
    
    return render(request, 'core/home.html', {
        'disenos': disenos,
        'servicios': servicios,
        'resenas': resenas,
    })

@login_required
def dashboard(request):
    """Panel administrativo para tu hermana"""
    hoy = date.today()
    
    citas_hoy = Cita.objects.filter(fecha=hoy)
    citas_pendientes = Cita.objects.filter(estado='pendiente')
    citas_confirmadas = Cita.objects.filter(estado='confirmada')
    resenas_pendientes = Resena.objects.filter(aprobada=False)
    
    # Estadísticas
    total_citas = Cita.objects.count()
    total_resenas = Resena.objects.count()
    total_disenos = Diseno.objects.count()
    total_servicios = Servicio.objects.count()
    
    context = {
        'citas_hoy': citas_hoy,
        'citas_pendientes': citas_pendientes,
        'citas_confirmadas': citas_confirmadas,
        'resenas_pendientes': resenas_pendientes,
        'total_citas': total_citas,
        'total_resenas': total_resenas,
        'total_disenos': total_disenos,
        'total_servicios': total_servicios,
    }
    return render(request, 'core/dashboard.html', context)
