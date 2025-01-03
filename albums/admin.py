from django.contrib import admin
from albums.models import Album

class AlbumAdmin(admin.ModelAdmin):
    list_display = ["id_album", "title", "artist", "release_date", "created_at"]
    search_fields = ["title", "artist", "release_date"]
    
admin.site.register(Album, AlbumAdmin)