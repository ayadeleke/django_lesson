from django.urls import path
from rest_framework.routers import DefaultRouter
from api.views import AuthorViewSet, AuthorList


router = DefaultRouter()
router.register('authors', AuthorViewSet)

urlpatterns = [
    path("authors/", AuthorList.as_view()),
] # + router.urls  ### Alternative URL configuration using viewsets, will need to remove the path to use this