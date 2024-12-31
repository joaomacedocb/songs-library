from django.contrib import admin

from artists.models import Artist

class ArtistAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "bio", "created_at", "updated_at"]
    search_fields = ["name"]
    
admin.site.register(Artist, ArtistAdmin)