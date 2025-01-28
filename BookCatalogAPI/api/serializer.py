from rest_framework import serializers

from api.models import Author, Book, Genre


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio', 'image']
        extra_kwargs = {'image': {'required': False}, }


class BookSerializer(serializers.ModelSerializer):
        author = AuthorSerializer(many=True)
        genre = serializers.StringRelatedField()
        class Meta:
         model = Book
         fields = ['id', 'title', 'author', 'year', 'genre', 'publisher', 'isbn', 'image', 'description']
         extra_kwargs = {'image': {'required': False}}


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

