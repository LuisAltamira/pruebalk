from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ArticleModelViewSet, CategoryModelViewSet

router = DefaultRouter()
router.register('article', ArticleModelViewSet, basename='articles')
router.register('category', CategoryModelViewSet, basename='categories')

urlpatterns = [
    # path('', include(router.urls))
]

urlpatterns += router.urls