from django.db import models
from uuid import uuid4

class Album(models.Model):
    id_album = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=100)
    artist = models.ForeignKey('artists.Artist', on_delete=models.CASCADE, related_name='albums')
    release_date = models.DateField(blank=True, null=True)
    cover = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.artist.name}\s {self.title}'
