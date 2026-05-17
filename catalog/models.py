"""
Modelos del catálogo Artist Beauty.

- Artist: artista/celebridad dueño/a de una marca de belleza, con su canción icónica.
- Category: tipo de producto (Skincare, Makeup, Fragrance, etc.).
- Product: producto del catálogo (lip oil, foundation, perfume, etc.).
"""
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.conf import settings
from django.db.models import Avg


class Category(models.Model):
    name = models.CharField('Nombre', max_length=80, unique=True)
    slug = models.SlugField(max_length=80, unique=True, blank=True)
    description = models.TextField('Descripción', blank=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Artist(models.Model):
    name = models.CharField('Nombre del/la artista', max_length=120)
    brand_name = models.CharField('Nombre de la marca', max_length=120)
    slug = models.SlugField(max_length=140, unique=True, blank=True)
    bio = models.TextField('Biografía', blank=True)
    image_url = models.URLField(
        'URL de la foto del artista', max_length=500, blank=True,
        help_text='Pega una URL pública. Si usas Cloudinary, usa el campo image.'
    )
    image = models.ImageField(
        'Imagen (Cloudinary)', upload_to='artists/', blank=True, null=True
    )
    iconic_song_title = models.CharField('Canción icónica', max_length=120)
    iconic_song_url = models.URLField(
        'URL del audio de la canción', max_length=500,
        help_text='URL directa a un mp3/preview (Spotify preview, Cloudinary, etc.)'
    )
    iconic_song_lyrics = models.TextField(
        'Letra de la canción icónica', blank=True,
        help_text='Letra (puede ser un fragmento). Se muestra en el detalle del artista.'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Artista'
        verbose_name_plural = 'Artistas'
        ordering = ['name']

    def __str__(self):
        return f'{self.name} — {self.brand_name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.brand_name}')
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('artist_detail', kwargs={'slug': self.slug})

    @property
    def display_image(self):
        """Devuelve la imagen disponible (Cloudinary o URL externa)."""
        if self.image:
            return self.image.url
        return self.image_url

    def bestsellers(self):
        """Top 5 productos best sellers de este artista."""
        return self.products.filter(is_bestseller=True).order_by('-rating', '-id')[:5]


class Product(models.Model):
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name='products',
        verbose_name='Artista/Marca'
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='products', verbose_name='Categoría'
    )
    name = models.CharField('Nombre del producto', max_length=160)
    slug = models.SlugField(max_length=180, unique=True, blank=True)
    description = models.TextField('Descripción')
    price = models.DecimalField('Precio (USD)', max_digits=8, decimal_places=2)
    image_url = models.URLField('URL de la imagen', max_length=500, blank=True)
    image = models.ImageField(
        'Imagen (Cloudinary)', upload_to='products/', blank=True, null=True
    )
    rating = models.DecimalField(
        'Rating', max_digits=3, decimal_places=1, default=4.5,
        help_text='De 0 a 5'
    )
    is_bestseller = models.BooleanField('¿Es best seller?', default=False)
    stock = models.PositiveIntegerField('Stock', default=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['-is_bestseller', '-rating', 'name']

    def __str__(self):
        return f'{self.name} ({self.artist.brand_name})'

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(f'{self.artist.brand_name}-{self.name}')
            self.slug = base[:180]
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

    @property
    def display_image(self):
        if self.image:
            return self.image.url
        return self.image_url

    @property
    def average_review_rating(self):
        avg = self.reviews.aggregate(a=Avg('rating'))['a']
        return round(avg, 1) if avg else None

    @property
    def reviews_count(self):
        return self.reviews.count()


# =========================================
# REVIEWS / COMENTARIOS
# =========================================
class Review(models.Model):
    """Comentario y calificación de un usuario sobre un producto."""
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='reviews'
    )
    rating = models.PositiveSmallIntegerField(
        'Calificación', default=5,
        choices=[(i, f'{i} ★') for i in range(1, 6)]
    )
    comment = models.TextField('Comentario')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        ordering = ['-created_at']
        # Una review por usuario y producto
        unique_together = [('product', 'user')]

    def __str__(self):
        return f'{self.user.username} → {self.product.name} ({self.rating}★)'


# =========================================
# WISHLIST / FAVORITOS
# =========================================
class WishlistItem(models.Model):
    """Relación usuario → producto favorito."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='wishlist'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='wishlist_items'
    )
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Favorito'
        verbose_name_plural = 'Favoritos'
        ordering = ['-added_at']
        unique_together = [('user', 'product')]

    def __str__(self):
        return f'{self.user.username} ♥ {self.product.name}'
