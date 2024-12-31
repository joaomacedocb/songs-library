from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from artists.api.viewsets import ArtistsViewSet

route = routers.DefaultRouter()
route.register(r'artists', ArtistsViewSet, 'Artists')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
