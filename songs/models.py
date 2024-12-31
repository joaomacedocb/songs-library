from django.db import models
from uuid import uuid4

class Song(models.Model):
    id_song = models.UUIDField(primary_key=True, default= uuid4, editable=False)
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    duration = models.DurationField()
    record = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)