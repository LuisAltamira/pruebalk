from rest_framework import serializers

from .models import Article, Category


class ArticleModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'


class CategoryModelSerializer(serializers.ModelSerializer):

    class Meta:
        model =  Category
        fields = ('name',)