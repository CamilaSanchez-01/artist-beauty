"""
URLs de la API REST: /api/...
"""
from rest_framework.routers import DefaultRouter
from .api_views import (ArtistViewSet, CategoryViewSet, ProductViewSet,
                        ReviewViewSet)

router = DefaultRouter()
router.register('artists', ArtistViewSet, basename='artist')
router.register('categories', CategoryViewSet, basename='category')
router.register('products', ProductViewSet, basename='product')
router.register('reviews', ReviewViewSet, basename='review')

urlpatterns = router.urls
