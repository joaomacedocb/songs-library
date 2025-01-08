from django.db import models
from uuid import uuid4

from artists.models import Artist
from albums.models import Album

class Genre(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

class Song(models.Model):
    id_song = models.UUIDField(primary_key=True, default= uuid4, editable=False)
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="songs")
    duration = models.DurationField(null=True, blank=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="songs")
    genres = models.ManyToManyField(Genre, related_name="songs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.title} by {self.artist}'