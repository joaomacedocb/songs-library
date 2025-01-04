from rest_framework import viewsets

from playlists.api.serializers import PlaylistsSerializers
from playlists.models import Playlist

class PlaylistsViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistsSerializers