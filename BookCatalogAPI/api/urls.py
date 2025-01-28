from django.urls import path
from rest_framework.routers import DefaultRouter
from api.views import AuthorViewSet, AuthorList, GenreList, GenreViewSet

router = DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('genres', GenreViewSet)

urlpatterns = [
    path("authors/", AuthorList.as_view()),
    path("genres/", GenreList.as_view()),
] # + router.urls  ### Alternative URL configuration using viewsets, will need to remove the path to use this