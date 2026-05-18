#!/usr/bin/env bash
# Script de build para Render
# Se ejecuta automáticamente en cada deploy

set -o errexit

pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# Carga datos de ejemplo solo si la base está vacía
python manage.py seed_data || true

# Crear Administradores
python manage.py shell -c "
from django.contrib.auth import get_user_model;
User = get_user_model();
username='Camilaadmin';
password='Cami123!';
email='sanchez.camila@uabc.edu.mx';
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
"
