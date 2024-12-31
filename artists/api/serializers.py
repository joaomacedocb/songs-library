from rest_framework import serializers

from artists.models import Artist

class ArtistsSerializer(serializers.Serializer):
    class Meta:
        model = Artist
        fields = "__all__"