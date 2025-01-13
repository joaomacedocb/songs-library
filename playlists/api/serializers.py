from rest_framework import serializers

from playlists.models import Playlist
from songs.models import Song


class SimplifiedSongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id_song','title']

class PlaylistsSerializers(serializers.ModelSerializer):
    songs = SimplifiedSongsSerializer(many= True, read_only=True)
    
    class Meta:
        model = Playlist
        fields = ['id', 'name', 'description', 'songs', 'owner', 'created_at', 'updated_at']