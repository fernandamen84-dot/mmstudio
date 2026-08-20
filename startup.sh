#!/bin/bash

echo "==> Ejecutando migraciones..."
python manage.py migrate --noinput

echo "==> Recopilando archivos estáticos..."
python manage.py collectstatic --noinput

echo "==> Iniciando servidor..."
gunicorn mmstudio.wsgi:application
