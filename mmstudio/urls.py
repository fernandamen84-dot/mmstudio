"""
URL configuration for mmstudio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Add the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse  # <-- AGREGADO PARA EL HANDLER500
from core import views
from citas import views as citas_views
from resenas import views as resenas_views
from configurador import views as configurador_views
from django.conf import settings
from django.conf.urls.static import static

# --- INICIO: CÓDIGO PARA CREAR EL ADMIN AUTOMÁTICAMENTE AL ARRANCAR ---
try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
    
    username = 'mmstudio'
    email = 'mmstudio@example.com'
    password = 'mmstudio2024'

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)
        print("✅ ¡ÉXITO! Superusuario 'mmstudio' creado desde urls.py.")
    else:
        print("ℹ️ El superusuario 'mmstudio' ya existe en la BD.")
except Exception as e:
    print(f"⚠️ Aviso: No se pudo crear el superusuario. Error: {e}")
# --- FIN: CÓDIGO PARA CREAR EL ADMIN ---


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('agendar/', citas_views.agendar_cita, name='agendar'),
    path('resenas/', resenas_views.ver_resenas, name='ver_resenas'),
    path('resenas/agregar/', resenas_views.agregar_resena, name='agregar_resena'),
    path('disenar/', configurador_views.disenar_uñas, name='disenar'),
]

# Solo en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Handler para errores 500 (Arreglado con el import de HttpResponse arriba)
def handler500(request, *args, **kwargs):
    return HttpResponse("Error 500 - Revisa los logs para más detalles.")
