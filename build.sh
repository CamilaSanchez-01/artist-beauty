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
