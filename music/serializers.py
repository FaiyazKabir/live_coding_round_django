from rest_framework import serializers
from django.contrib.auth.models import User 
from music.models import Playlist,Songs
from django.contrib.auth.models import User
from django_grpc_framework import proto_serializers
import music.account.account_pb2
import music.playlist.playlist_pb2 as playlist_pb2

class Userserializer(serializers.ModelSerializer):
	total_playlists_count = serializers.SerializerMethodField()

	def get_total_playlists_count(self,object):
		return len(Playlist.objects.filter(user_id=object["id"]))

	class Meta:
		model = User
		fields = '__all__' 

class NewUserserializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields=['username', 'email']

class PlaylistSerializer(serializers.ModelSerializer):
	total_songs_count = serializers.SerializerMethodField()
	user = NewUserserializer(many=False)
	def get_total_songs_count(self,object):
		return len(Songs.objects.filter(playlist_id=object.id))

	class Meta:
		model = Playlist
		fields = '__all__'


class NewPlaylistSerializer(serializers.ModelSerializer):
	user = NewUserserializer(many=False)
	class Meta:
		model = Playlist
		fields= '__all__'

class SongsSerializer(serializers.ModelSerializer):
	playlist = NewPlaylistSerializer(many=False)
	class Meta:
		model = Songs
		fields = '__all__'


class UserProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = User
        proto_class = music.account.account_pb2.User
        fields = ['username', 'email', 'groups']
	
class PlaylistProtoSerializer(proto_serializers.ModelProtoSerializer):
	total_songs_count = serializers.SerializerMethodField()
	user = UserProtoSerializer(many=False)
	def get_total_songs_count(self,object):
		return len(Songs.objects.filter(playlist_id=object.id))

	class Meta:
		model = Playlist
		proto_class = playlist_pb2.Playlist
		fields = ['name','user','total_songs_count']
		# extra_kwargs = {'user': {'required': False},'name': {'required': False}}