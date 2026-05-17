"""
Vistas web (HTML) del catálogo.
CRUD completo de artistas y productos.
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.db.models import Q, Count
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .models import Artist, Category, Product, Review, WishlistItem
from .forms import (ArtistForm, ProductForm, CategoryForm,
                    ReviewForm, SignupForm)
from .music import get_product_audio


# =========================================
# HOME / LISTADOS
# =========================================
def home(request):
    artists = Artist.objects.all()
    categories = Category.objects.all()
    bestsellers = Product.objects.filter(
        is_bestseller=True).select_related('artist')[:8]
    return render(request, 'catalog/home.html', {
        'artists': artists,
        'categories': categories,
        'bestsellers': bestsellers,
    })


def artist_detail(request, slug):
    """Página clave: muestra al artista, sus 5 best sellers y reproduce su canción."""
    artist = get_object_or_404(Artist, slug=slug)
    bestsellers = artist.bestsellers()
    other_products = artist.products.exclude(
        id__in=[p.id for p in bestsellers])
    return render(request, 'catalog/artist_detail.html', {
        'artist': artist,
        'bestsellers': bestsellers,
        'other_products': other_products,
    })


def product_list(request):
    products = Product.objects.select_related('artist', 'category')
    q = request.GET.get('q', '')
    cat = request.GET.get('category', '')
    if q:
        products = products.filter(
            Q(name__icontains=q) | Q(description__icontains=q)
            | Q(artist__brand_name__icontains=q)
        )
    if cat:
        products = products.filter(category__slug=cat)
    return render(request, 'catalog/product_list.html', {
        'products': products,
        'categories': Category.objects.all(),
        'q': q,
        'current_category': cat,
    })


def product_detail(request, slug):
    product = get_object_or_404(
        Product.objects.select_related('artist', 'category'), slug=slug)
    reviews = product.reviews.select_related('user').all()
    user_review = None
    review_form = None
    in_wishlist = False
    if request.user.is_authenticated:
        user_review = reviews.filter(user=request.user).first()
        in_wishlist = WishlistItem.objects.filter(
            user=request.user, product=product).exists()
        if request.method == 'POST':
            review_form = ReviewForm(request.POST, instance=user_review)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.product = product
                review.user = request.user
                review.save()
                messages.success(request, '¡Gracias por tu review!')
                return redirect(product.get_absolute_url())
        else:
            review_form = ReviewForm(instance=user_review)

    page_song_url, page_song_title = get_product_audio(product)
    return render(request, 'catalog/product_detail.html', {
        'product': product,
        'reviews': reviews,
        'review_form': review_form,
        'user_review': user_review,
        'in_wishlist': in_wishlist,
        'page_song_url': page_song_url,
        'page_song_title': page_song_title,
    })


# =========================================
# PLAYLIST
# =========================================
def playlist(request):
    """Página tipo Spotify con todas las canciones de las marcas."""
    artists = Artist.objects.exclude(iconic_song_url='')
    return render(request, 'catalog/playlist.html', {'artists': artists})


# =========================================
# WISHLIST
# =========================================
@login_required
def wishlist(request):
    items = WishlistItem.objects.filter(
        user=request.user).select_related('product__artist', 'product__category')
    return render(request, 'catalog/wishlist.html', {'items': items})


@require_POST
@login_required
def wishlist_toggle(request, slug):
    """AJAX: agrega o quita un producto de favoritos. Devuelve JSON."""
    product = get_object_or_404(Product, slug=slug)
    item, created = WishlistItem.objects.get_or_create(
        user=request.user, product=product)
    if not created:
        item.delete()
        return JsonResponse({'in_wishlist': False, 'action': 'removed'})
    return JsonResponse({'in_wishlist': True, 'action': 'added'})


# =========================================
# SIGNUP
# =========================================
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'¡Bienvenida {user.username}!')
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


# =========================================
# CRUD ARTISTAS (requiere login)
# =========================================
@login_required
def artist_create(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            artist = form.save()
            messages.success(request, f'Artista "{artist.name}" creado.')
            return redirect(artist.get_absolute_url())
    else:
        form = ArtistForm()
    return render(request, 'catalog/form.html', {
        'form': form, 'title': 'Nuevo artista'})


@login_required
def artist_edit(request, slug):
    artist = get_object_or_404(Artist, slug=slug)
    if request.method == 'POST':
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            form.save()
            messages.success(request, 'Artista actualizado.')
            return redirect(artist.get_absolute_url())
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'catalog/form.html', {
        'form': form, 'title': f'Editar {artist.name}'})


@login_required
def artist_delete(request, slug):
    artist = get_object_or_404(Artist, slug=slug)
    if request.method == 'POST':
        artist.delete()
        messages.success(request, 'Artista eliminado.')
        return redirect('home')
    return render(request, 'catalog/confirm_delete.html', {
        'object': artist, 'type': 'artista'})


# =========================================
# CRUD PRODUCTOS
# =========================================
@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            messages.success(request, f'Producto "{product.name}" creado.')
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'catalog/form.html', {
        'form': form, 'title': 'Nuevo producto'})


@login_required
def product_edit(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado.')
            return redirect(product.get_absolute_url())
    else:
        form = ProductForm(instance=product)
    return render(request, 'catalog/form.html', {
        'form': form, 'title': f'Editar {product.name}'})


@login_required
def product_delete(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Producto eliminado.')
        return redirect('product_list')
    return render(request, 'catalog/confirm_delete.html', {
        'object': product, 'type': 'producto'})
