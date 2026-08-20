#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mmstudio.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


# --- INICIO DE CÓDIGO PARA CREAR SUPERUSUARIO AUTOMÁTICAMENTE ---
if __name__ == '__main__':
    # Esto solo se ejecutará si ejecutamos un comando (como el deploy de Render o migrate)
    # Verificamos si el comando es uno de los comunes para evitar errores raros al iniciar
    if len(sys.argv) > 1 and sys.argv[1] in ['runserver', 'migrate', 'collectstatic']:
        try:
            # Configuramos el entorno de Django para poder usar los modelos
            os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mmstudio.settings')
            import django
            django.setup()

            from django.contrib.auth import get_user_model
            User = get_user_model()

            username = 'mmstudio'
            email = 'mmstudio@example.com'
            password = 'mmstudio2024'

            if not User.objects.filter(username=username).exists():
                User.objects.create_superuser(username, email, password)
                print(f"✅ Superusuario '{username}' creado con éxito!")
            else:
                print(f"ℹ️ El superusuario '{username}' ya existe.")
        except Exception as e:
            # Si falla, no detenemos el despliegue, solo mostramos el error
            print(f"⚠️ Aviso: No se pudo verificar/crear el superusuario. Error: {e}")

    main()
# --- FIN DE CÓDIGO ---
