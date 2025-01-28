from django.urls import path
from rest_framework.routers import DefaultRouter
from api.views import AuthorViewSet, GenreViewSet, BookViewSet

router = DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('genres', GenreViewSet)
router.register('books', BookViewSet)

urlpatterns = [
    # path("authors/", AuthorList.as_view()),
    # path("genres/", GenreList.as_view()),
    # path("books/", BookList.as_view()),
]  + router.urls  ### Alternative URL configuration using viewsets, will need to remove the path to use this