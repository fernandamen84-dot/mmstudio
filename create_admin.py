import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mmstudio.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = 'admin'
email = 'admin@example.com'
password = 'admin123456'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f'✅ Superusuario "{username}" creado con éxito!')
else:
    print(f'ℹ️ El superusuario "{username}" ya existe.')
