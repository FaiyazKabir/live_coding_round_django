from django.conf import settings
from django.urls import path
from music.views import SongsList,PlaylistList,UserList

urlpatterns = [
    path('songs',SongsList.as_view()),
    path('playlists',PlaylistList.as_view()),
    path('users',UserList.as_view())
]
