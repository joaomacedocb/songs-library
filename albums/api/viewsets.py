from rest_framework import viewsets

from albums.api.serializers import AlbumsSerializer
from albums.models import Album

class AlbumsViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumsSerializer