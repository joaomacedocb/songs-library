from rest_framework import serializers

from albums.models import Album

class AlbumsSerializer(serializers.ModelSerializer):
    artist_name = serializers.CharField(source='artist.name', read_only = True)
    
    class Meta:
        model = Album
        fields = ['id_album', 'title', 'artist', 'artist_name', 'release_date', 'created_at']