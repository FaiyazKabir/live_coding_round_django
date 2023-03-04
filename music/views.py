from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from music.models import Songs
from music.models import Playlist
from django.contrib.auth.models import User 
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
		playlist = Playlist.objects.select_related("user").all().values()
		return Response({
			"data":playlist,
			"status":status.HTTP_200_OK
			})

class UserList(APIView):
	permission_classes = [AllowAny]
	def get(self,request):
		users = User.objects.all().values()
		return Response({
			"data":users,
			"status":status.HTTP_200_OK
			})

