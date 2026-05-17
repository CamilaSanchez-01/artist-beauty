"""
ViewSets de la API REST.
"""
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Artist, Category, Product, Review
from .serializers import (
    ArtistSerializer, CategorySerializer, ProductSerializer, ReviewSerializer
)


class ReviewViewSet(viewsets.ModelViewSet):
    """CRUD de reviews."""
    queryset = Review.objects.select_related('user', 'product').all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            serializer.save()


class CategoryViewSet(viewsets.ModelViewSet):
    """CRUD completo de categorías."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class ArtistViewSet(viewsets.ModelViewSet):
    """CRUD completo de artistas/marcas."""
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    lookup_field = 'slug'
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'brand_name', 'iconic_song_title']
    ordering_fields = ['name', 'created_at']

    @action(detail=True, methods=['get'])
    def bestsellers(self, request, slug=None):
        """GET /api/artists/{slug}/bestsellers/ — top 5 best sellers + audio."""
        artist = self.get_object()
        serializer = ProductSerializer(artist.bestsellers(), many=True)
        return Response({
            'artist': artist.name,
            'brand': artist.brand_name,
            'iconic_song_title': artist.iconic_song_title,
            'iconic_song_url': artist.iconic_song_url,
            'bestsellers': serializer.data,
        })


class ProductViewSet(viewsets.ModelViewSet):
    """CRUD completo de productos."""
    queryset = Product.objects.select_related('artist', 'category')
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description', 'artist__brand_name']
    ordering_fields = ['price', 'rating', 'created_at']

    def get_queryset(self):
        qs = super().get_queryset()
        is_bs = self.request.query_params.get('bestseller')
        category = self.request.query_params.get('category')
        artist = self.request.query_params.get('artist')
        if is_bs in ('1', 'true', 'True'):
            qs = qs.filter(is_bestseller=True)
        if category:
            qs = qs.filter(category__slug=category)
        if artist:
            qs = qs.filter(artist__slug=artist)
        return qs

    @action(detail=False, methods=['get'])
    def bestsellers(self, request):
        """GET /api/products/bestsellers/ — todos los best sellers."""
        qs = self.get_queryset().filter(is_bestseller=True)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)
