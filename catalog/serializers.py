"""
Serializers de la API REST para Artist Beauty.
"""
from rest_framework import serializers
from .models import Artist, Category, Product, Review


class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'product', 'product_name', 'user', 'username',
                  'rating', 'comment', 'created_at']
        read_only_fields = ['user', 'created_at']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description']
        read_only_fields = ['slug']


class ProductSerializer(serializers.ModelSerializer):
    artist_name = serializers.CharField(source='artist.name', read_only=True)
    brand_name = serializers.CharField(source='artist.brand_name', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    iconic_song_url = serializers.CharField(
        source='artist.iconic_song_url', read_only=True)
    iconic_song_title = serializers.CharField(
        source='artist.iconic_song_title', read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'description', 'price',
            'image_url', 'rating', 'is_bestseller', 'stock',
            'artist', 'artist_name', 'brand_name',
            'category', 'category_name',
            'iconic_song_url', 'iconic_song_title',
            'created_at', 'updated_at',
        ]
        read_only_fields = ['slug', 'created_at', 'updated_at']


class ArtistSerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()
    bestsellers = serializers.SerializerMethodField()

    class Meta:
        model = Artist
        fields = [
            'id', 'name', 'brand_name', 'slug', 'bio',
            'image_url', 'iconic_song_title', 'iconic_song_url',
            'iconic_song_lyrics',
            'products_count', 'bestsellers', 'created_at',
        ]
        read_only_fields = ['slug', 'created_at']

    def get_products_count(self, obj):
        return obj.products.count()

    def get_bestsellers(self, obj):
        return ProductSerializer(obj.bestsellers(), many=True).data
