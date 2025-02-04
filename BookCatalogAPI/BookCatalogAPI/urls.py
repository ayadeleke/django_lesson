from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from api.views import list_authors, GenreViewSet, BookViewSet

# router = DefaultRouter()
# router.register('authors', AuthorViewSet)
# router.register('genres', GenreViewSet)
# router.register('books', BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
   path('api/authors/', list_authors),
   #  path('api/genres/', list_genres),
   #  path('api/books/', list_books),
   # path('api/authors/', AuthorList.as_view()), ### Alternative URL configuration using class-based views
   #  path('api/', include('api.urls')),
] #+ router.urls ### Alternative URL configuration using viewsets
