from rest_framework import viewsets

from artists.api.serializers import ArtistsSerializer
from artists.models import Artist

class ArtistsViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistsSerializer
    