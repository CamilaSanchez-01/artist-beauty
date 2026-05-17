"""
URLs web (HTML) del catálogo.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('playlist/', views.playlist, name='playlist'),
    path('mis-favoritos/', views.wishlist, name='wishlist'),
    path('mis-favoritos/toggle/<slug:slug>/', views.wishlist_toggle, name='wishlist_toggle'),
    path('registrarse/', views.signup, name='signup'),

    path('artistas/nuevo/', views.artist_create, name='artist_create'),
    path('artistas/<slug:slug>/', views.artist_detail, name='artist_detail'),
    path('artistas/<slug:slug>/editar/', views.artist_edit, name='artist_edit'),
    path('artistas/<slug:slug>/eliminar/', views.artist_delete, name='artist_delete'),

    path('productos/', views.product_list, name='product_list'),
    path('productos/nuevo/', views.product_create, name='product_create'),
    path('productos/<slug:slug>/', views.product_detail, name='product_detail'),
    path('productos/<slug:slug>/editar/', views.product_edit, name='product_edit'),
    path('productos/<slug:slug>/eliminar/', views.product_delete, name='product_delete'),
]
