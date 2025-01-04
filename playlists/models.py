from uuid import uuid4
from django.db import models
from django.contrib.auth import get_user_model

from songs.models import Song

User = get_user_model()

class Playlist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=500)
    songs = models.ManyToManyField(Song, related_name='playlists')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlists')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):  
        return f'{self.owner}\' {self.name} Playlist'
    
