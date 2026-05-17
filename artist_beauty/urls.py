"""
URLs raíz del proyecto Artist Beauty.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from catalog.views import signup as signup_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls')),
    path('api/', include('catalog.api_urls')),

    # Autenticación básica
    path('accounts/login/', auth_views.LoginView.as_view(
        template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/signup/', signup_view, name='signup'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
