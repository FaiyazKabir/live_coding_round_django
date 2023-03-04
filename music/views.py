from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from music.models import Songs
from music.models import Playlist
from django.contrib.auth.models import User 
from music.serializers import Userserializer,PlaylistSerializer

# Create your views here.
class SongsList(APIView):
	permission_classes = [AllowAny]
	def get(self,request):
		songs = Songs.objects.select_related("playlist").all().values()
		return Response({
			"data":songs,
			"status":status.HTTP_200_OK
			})


class PlaylistList(APIView):
	permission_classes = [AllowAny]
	def get(self,request):
		playlist = Playlist.objects.all().values()

		data = PlaylistSerializer(playlist,many=True).data
		return Response({
			"data":data,
			"status":status.HTTP_200_OK
			})

class UserList(APIView):
	permission_classes = [AllowAny]
	def get(self,request):
		users = User.objects.all().values()

		data = Userserializer(users,many=True).data
		# new_users_list = []
		# for user in users:
		# 	playlist_count = len(Playlist.objects.filter(user = user))
			
		# 	new_users_list.append({

		# 		})

		return Response({
			"data":data,
			"status":status.HTTP_200_OK
			})

