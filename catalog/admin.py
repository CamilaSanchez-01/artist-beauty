from django.contrib import admin
from .models import Artist, Category, Product, Review, WishlistItem


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('comment', 'product__name', 'user__username')


@admin.register(WishlistItem)
class WishlistItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'added_at')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand_name', 'iconic_song_title', 'created_at')
    prepopulated_fields = {'slug': ('name', 'brand_name')}
    search_fields = ('name', 'brand_name', 'iconic_song_title')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist', 'category', 'price',
                    'rating', 'is_bestseller', 'stock')
    list_filter = ('is_bestseller', 'category', 'artist')
    search_fields = ('name', 'description')
    list_editable = ('price', 'is_bestseller', 'stock')
    prepopulated_fields = {'slug': ('name',)}
