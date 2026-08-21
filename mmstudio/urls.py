from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from core import views
from citas import views as citas_views
from resenas import views as resenas_views
from configurador import views as configurador_views
from catalogo import views as catalogo_views
from django.conf import settings
from django.conf.urls.static import static

# --- CODIGO PARA CREAR EL ADMIN AUTOMATICAMENTE AL ARRANCAR ---
try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
    
    username = 'mmstudio'
    email = 'mmstudio@example.com'
    password = 'mmstudio2024'

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)
        print("SUPERUSUARIO CREADO: mmstudio / mmstudio2024")
    else:
        print("El superusuario mmstudio ya existe")
except Exception as e:
    print(f"No se pudo crear el superusuario: {e}")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    
    # Autenticacion
    path('login/', LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    
    # Clientes
    path('agendar/', citas_views.agendar_cita, name='agendar'),
    path('resenas/', resenas_views.ver_resenas, name='ver_resenas'),
    path('resenas/agregar/', resenas_views.agregar_resena, name='agregar_resena'),
    path('disenar/', configurador_views.disenar_uñas, name='disenar'),
    
    # Dashboard - Panel de control para tu hermana
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/citas/', citas_views.gestionar_citas, name='gestionar_citas'),
    path('dashboard/citas/<int:cita_id>/<str:estado>/', citas_views.cambiar_estado_cita, name='cambiar_estado_cita'),
    path('dashboard/resenas/', resenas_views.gestionar_resenas, name='gestionar_resenas'),
    path('dashboard/resenas/aprobar/<int:resena_id>/', resenas_views.aprobar_resena, name='aprobar_resena'),
    path('dashboard/resenas/eliminar/<int:resena_id>/', resenas_views.eliminar_resena, name='eliminar_resena'),
    path('dashboard/diseno/nuevo/', catalogo_views.agregar_diseno, name='agregar_diseno'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

def handler500(request, *args, **kwargs):
    return HttpResponse("Error 500 - Revisa los logs para mas detalles.")
