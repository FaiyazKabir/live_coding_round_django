from django.contrib import admin

from music.models import Playlist, Songs

# Register your models here.

class Playlistadmin(admin.ModelAdmin):
    model = Playlist

class Songsadmin(admin.ModelAdmin):
    model = Songs

admin.site.register(Playlist,Playlistadmin)
admin.site.register(Songs,Songsadmin)