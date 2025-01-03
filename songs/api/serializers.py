from rest_framework import serializers

from songs.models import Song, Genre

class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"

class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"