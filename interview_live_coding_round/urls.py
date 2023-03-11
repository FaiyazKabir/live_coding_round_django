"""interview_live_coding_round URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
import music.account.account_pb2_grpc as account_pb2_grpc
import music.playlist.playlist_pb2_grpc as playlist_pb2_grpc
from music.services import UserService,PlaylistService

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include("music.urls"))
]

def grpc_handlers(server):
    account_pb2_grpc.add_UserControllerServicer_to_server(UserService.as_servicer(), server)
    playlist_pb2_grpc.add_PlaylistControllerServicer_to_server(PlaylistService.as_servicer(),server)