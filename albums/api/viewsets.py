from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from albums.api.serializers import AlbumDetalhesSerializer, AlbumsSerializer
from albums.models import Album

class AlbumsViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumsSerializer
    
    @action(detail=True, methods=['get'])
    def details(self, request, pk=None, *args, **kwargs):
        album = get_object_or_404(Album, pk=pk)
        serializer = AlbumDetalhesSerializer(album)
        return Response(serializer.data)
    
