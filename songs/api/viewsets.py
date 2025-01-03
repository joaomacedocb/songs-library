from rest_framework import viewsets

from songs.api.serializers import SongsSerializer, GenresSerializer
from songs.models import Song, Genre

class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenresSerializer

class SongsViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongsSerializer