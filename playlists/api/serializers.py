from rest_framework import serializers

from playlists.models import Playlist

class PlaylistsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = "__all__"