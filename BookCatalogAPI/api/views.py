from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from rest_framework import viewsets, status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_redis import cache
from api.models import Author, Genre, Book
from api.serializer import AuthorSerializer, GenreSerializer, BookSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

### Function based views for the Author model ###
@api_view(['POST', 'GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@cache_page(30)
def list_authors(request):
    if request.method == 'POST':
        # Create a new author
        data = request.data
        # Serialize the data
        serializer = AuthorSerializer(data=data)

        # Check if the data is valid
        if serializer.is_valid():
            # Save the data to the database
            serializer.save()
            cache.delete_pattern("*")
            # Return a success response
            return Response({"message": "Author created successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)

    else:
        # Get list of authors from the database
        authors = Author.objects.all()

        # Apply pagination
        paginator = PageNumberPagination()
        paginator.page_size = 5
        paginated_authors = paginator.paginate_queryset(authors, request)

        # Serialize the list of authors to JSON
        serializer = AuthorSerializer(paginated_authors, many=True)
        # Return the serialized paginated data
        return paginator.get_paginated_response(serializer.data)

### Class-based views to achieve the same result:# ##
# class AuthorList(APIView):
#     def get(self, request):
#         authors = Author.objects.all()
#         serializer = AuthorSerializer(authors, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         data = request.data
#         serializer = AuthorSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

### Alternatively, you can use viewset to achieve the same result:# ##
# class AuthorViewSet(viewsets.ModelViewSet):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]

### View for the Genre model ###
# class GenreList(APIView):
#     def get(self, request):
#         genres = Genre.objects.all()
#         serializer = GenreSerializer(genres, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         data = request.data
#         serializer = GenreSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

### Function based views for the Genre model ###
# @api_view(['POST', 'GET'])
# @authentication_classes([BasicAuthentication])
# @permission_classes([IsAuthenticated])
# def list_genres(request):
#     if request.method == 'POST':
#         # Create a new genre
#         data = request.data
#         # Serialize the data
#         serializer = GenreSerializer(data=data)
#
#         # Check if the data is valid
#         if serializer.is_valid():
#             # Save the data to the database
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#     else:
#         # Get list of genres from the database
#         genres = Genre.objects.all()
#         # Serialize the list of genres to JSON
#         serializer = GenreSerializer(genres, many=True)
#         # Return the serialized data
#         return Response(serializer.data)

### Alternatively, you can use viewset to achieve the same result:# ##
class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

### Function based views for the Book model ###
# @api_view(['POST', 'GET'])
# @authentication_classes([BasicAuthentication])
# @permission_classes([IsAuthenticated])
# def list_books(request):
#     if request.method == 'POST':
#         # Create a new book
#         data = request.data
#         # Serialize the data
#         serializer = BookSerializer(data=data)
#
#         # Check if the data is valid
#         if serializer.is_valid():
#             # Save the data to the database
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#     else:
#         # Get list of books from the database
#         books = Book.objects.all()
#         # Serialize the list of books to JSON
#         serializer = BookSerializer(books, many=True)
#         # Return the serialized data
#         return Response(serializer.data)

### Class-based views to achieve the same result:# ##
# class BookList(APIView):
#     def get(self, request):
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         data = request.data
#         serializer = BookSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

### Alternatively, you can use viewset to achieve the same result:# ##
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

def my_view(request):
    # Store data for 60 seconds
    cache.set("django_test_key", "Django and Redis work!", 60)
    value = cache.get("django_test_key")  # Should print the value
    return HttpResponse(value)