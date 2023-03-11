from django.conf import settings
from django.urls import path
from music.views import SongsList,PlaylistList,UserList
# import serveraccount_pb2_grpc
from music.services import UserService


urlpatterns = [
    path('songs',SongsList.as_view()),
    path('playlists',PlaylistList.as_view()),
    path('users',UserList.as_view())
]


# def grpc_handlers(server):
#     account_pb2_grpc.add_UserControllerServicer_to_server(UserService.as_servicer(), server)