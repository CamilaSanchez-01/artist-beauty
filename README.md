# 🌸 Artist Beauty — Catálogo Web

Proyecto académico (Meta 4.3) — Aplicación web con Django + API REST + reproductor de audio.

## ✨ Concepto

Catálogo de marcas de **make up y skincare** creadas por artistas famosos
(Rare Beauty, Fenty Beauty, R.E.M Beauty, Pleasing, Florence by Mills).
Al entrar al perfil de un artista, se reproduce automáticamente su canción icónica
mientras se ven sus 5 productos más vendidos.

## 🚀 Demo

URL pública: **(agregar después del despliegue en Render)**

Repositorio: **(agregar tu URL de GitHub)**

## 🛠 Tecnologías

- **Backend**: Django 5.0, Django REST Framework
- **Base de datos**: SQLite (dev) / PostgreSQL (Render)
- **Frontend**: HTML5, CSS3 (Playfair + Poppins), JavaScript vanilla
- **Audio**: HTML5 Audio API + IntersectionObserver
- **Imágenes**: Cloudinary (opcional) o URLs directas
- **Despliegue**: Render (Gunicorn + WhiteNoise)

## 📦 Instalación local

```bash
git clone <repo>
cd artist_beauty
python -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_data
python manage.py createsuperuser
python manage.py runserver
```

Abrir http://localhost:8000

## 📡 Endpoints principales de la API

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/artists/` | Lista de artistas/marcas |
| POST | `/api/artists/` | Crear artista |
| GET | `/api/artists/{slug}/` | Detalle de artista |
| PUT/PATCH | `/api/artists/{slug}/` | Editar artista |
| DELETE | `/api/artists/{slug}/` | Eliminar artista |
| GET | `/api/artists/{slug}/bestsellers/` | Top 5 + canción icónica |
| GET | `/api/products/` | Lista de productos |
| POST | `/api/products/` | Crear producto |
| GET | `/api/products/{slug}/` | Detalle de producto |
| GET | `/api/products/bestsellers/` | Todos los best sellers |
| GET | `/api/products/?category=skincare` | Filtrar por categoría |
| GET | `/api/categories/` | Lista de categorías |

Interfaz navegable: `/api/` (Browsable API de DRF)

## 🆕 Mejoras vs Actividad 3.2

1. **Reproductor de audio automático** con HTML5 Audio + IntersectionObserver
2. **Cloudinary** para almacenamiento de imágenes (opcional)
3. **Categorías** con filtrado dinámico
4. **Autenticación** de usuarios para operaciones CRUD
5. **Diseño visual responsivo** con paleta cohesiva
6. **API enriquecida** con endpoint custom de best sellers por artista
