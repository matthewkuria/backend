from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import News, NewsCategory

class NewsCategorySerializer(serializers.ModelSerializer):
    """Serializer for NewsCategory model."""
    class Meta:
        model = NewsCategory
        fields = ['id', 'name']


class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for the author field to display basic user information."""
    class Meta:
        model = get_user_model()
        fields = ['id',  'email']


class NewsSerializer(serializers.ModelSerializer):
    """Serializer for the News model with nested category and author details."""
    category = NewsCategorySerializer(read_only=True)  # Nested serializer for category
    author = AuthorSerializer(read_only=True)  # Nested serializer for author details
    tags = serializers.ListField(child=serializers.CharField(), required=False)  # Convert comma-separated tags to list
    
    class Meta:
        model = News
        fields = [
            'id', 'title', 'slug', 'content', 'summary', 'category', 'author', 'created_at', 
            'updated_at', 'published_date', 'image', 'tags', 'view_count', 'is_featured'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'view_count']

    def to_representation(self, instance):
        """Customize representation to display tags as a list."""
        representation = super().to_representation(instance)
        representation['tags'] = instance.get_tags_list()
        return representation
