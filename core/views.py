from django.shortcuts import render
from catalogo.models import Diseno, Servicio
from resenas.models import Resena

def home(request):
    disenos_recientes = Diseno.objects.filter(activo=True)[:6]
    servicios = Servicio.objects.filter(activo=True)
    resenas_aprobadas = Resena.objects.filter(aprobada=True)
    
    return render(request, 'core/home.html', {
        'disenos': disenos_recientes,
        'servicios': servicios,
        'resenas_aprobadas': resenas_aprobadas,
    })