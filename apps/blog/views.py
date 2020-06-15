from django.shortcuts import render
from rest_framework import viewsets

from .models import Article, Category
from .serializers import ArticleModelSerializer, CategoryModelSerializer


class ArticleModelViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
