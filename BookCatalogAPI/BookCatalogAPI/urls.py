from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from api.views import AuthorList, AuthorViewSet, list_authors, GenreList, GenreViewSet

router = DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('genres', GenreViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
#    path('api/authors/', list_authors),
#    path('api/authors/', AuthorList.as_view()), ### Alternative URL configuration using class-based views
    path('api/', include('api.urls')),
] + router.urls ### Alternative URL configuration using viewsets
