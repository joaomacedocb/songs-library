from rest_framework import serializers

from songs.models import Song, Genre
from albums.models import Album

class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"

class SongsSerializer(serializers.ModelSerializer):
    
    artist_name = serializers.CharField(source='artist.name', read_only = True)
    album_name = serializers.CharField(source='album.title', read_only = True)
    
    class Meta:
        model = Song
        fields = [
        'id_song', 'title', 'artist', 'artist_name', 'duration', 
        'album', 'album_name', 'genres', 'created_at', 'updated_at'
        ]