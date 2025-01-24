from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Author
from api.serializer import AuthorSerializer

from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Author
from api.serializer import AuthorSerializer
from rest_framework.views import APIView


@api_view(['POST', 'GET'])
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
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    else:
        # Get list of authors from the database
        authors = Author.objects.all()
        # Serialize the list of authors to JSON
        serializer = AuthorSerializer(authors, many=True)
        # Return the serialized data
        return Response(serializer.data)

### Alternatively, you can use class-based views to achieve the same result:# ##

class AuthorList(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = AuthorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

### Alternatively, you can use viewset to achieve the same result:# ##

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer