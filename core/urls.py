from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from artists.api.viewsets import ArtistsViewSet
from albums.api.viewsets import AlbumsViewSet

route = routers.DefaultRouter()

route.register(r'artists', ArtistsViewSet, 'Artists')
route.register(r'albums', AlbumsViewSet, 'Albums')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
