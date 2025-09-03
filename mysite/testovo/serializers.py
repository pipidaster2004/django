from rest_framework import serializers
from .models import Book, Author

class BookSerializer(serializers.ModelSerializer):
    """
    сериализатор для модели книг
    """
    author_name = serializers.CharField(source='author.__str__', read_only=True)
    class Meta:
        model = Book
        fields = ('title', 'author_name', 'published_date', 'price')

class AuthorSerializer(serializers.ModelSerializer):
    """
    сериализатор для модели автора
    """
    class Meta:
        model = Author
        fields = '__all__'