from rest_framework import serializers

from albums.models import Album
from songs.api.serializers import SongsSerializer

class AlbumsSerializer(serializers.ModelSerializer):
    artist_name = serializers.CharField(source='artist.name', read_only = True)
    
    class Meta:
        model = Album
        fields = ['id_album', 'title', 'artist', 'artist_name', 'release_date', 'created_at']
        
class AlbumDetalhesSerializer(serializers.ModelSerializer):
    
    songs = SongsSerializer(many=True, read_only = True)
    artist_name = serializers.CharField(source='artist.name', read_only = True)
    
    class Meta:

        
        model = Album
        fields = ['id_album', 'title', 'artist', 'artist_name', 'songs']