from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from artists.api.viewsets import ArtistsViewSet
from albums.api.viewsets import AlbumsViewSet
from playlists.api.viewsets import PlaylistsViewSet
from songs.api.viewsets import GenresViewSet, SongsViewSet

route = routers.DefaultRouter()

route.register(r'artists', ArtistsViewSet, 'Artists')
route.register(r'albums', AlbumsViewSet, 'Albums')
route.register(r'genres', GenresViewSet, 'Genres')
route.register(r'songs', SongsViewSet, 'Songs')
route.register(r'playlists', PlaylistsViewSet, 'Playlists')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
