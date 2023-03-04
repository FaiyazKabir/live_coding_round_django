from rest_framework import serializers
from django.contrib.auth.models import User 
from music.models import Playlist,Songs

class Userserializer(serializers.ModelSerializer):
	total_playlists_count = serializers.SerializerMethodField()

	def get_total_playlists_count(self,object):
		return len(Playlist.objects.filter(user_id=object["id"]))

	class Meta:
		model = User
		fields = '__all__' 

class PlaylistSerializer(serializers.ModelSerializer):
	total_songs_count = serializers.SerializerMethodField()

	def get_total_songs_count(self,object):
		return len(Songs.objects.filter(playlist_id=object["id"]))

	class Meta:
		model = Playlist
		fields = '__all__'