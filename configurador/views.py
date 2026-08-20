from django.shortcuts import render
from .models import FormaUña, ColorUña, DisenoPersonalizado
from catalogo.models import Servicio

def disenar_uñas(request):
    formas = FormaUña.objects.all()
    colores = ColorUña.objects.all()
    disenos = DisenoPersonalizado.objects.all()
    servicios = Servicio.objects.filter(activo=True)
    
    context = {
        'formas': formas,
        'colores': colores,
        'disenos': disenos,
        'servicios': servicios,
    }
    return render(request, 'configurador/disenar.html', context)