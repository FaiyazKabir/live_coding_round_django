from django.contrib.auth.models import User
from django_grpc_framework import generics
from music.models import Playlist
from music.serializers import UserProtoSerializer,PlaylistProtoSerializer


class UserService(generics.ModelService):
    """
    gRPC service that allows users to be retrieved or updated.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserProtoSerializer

class PlaylistService(generics.ModelService):
    def List(self,request,context):
        print("LINE 16")
        queryset = Playlist.objects.all()
        serializer_class = PlaylistProtoSerializer(queryset,many=True)
        for msg in serializer_class.message:
            yield msg

    def Retrieve(self, request, context):
        print("LINE 22")
        playlist = Playlist.objects.get(id=request.id)
        serializer = PlaylistProtoSerializer(playlist)
        # serializer.is_valid(raise_exception=False)
        print("LINE 24",serializer.data)
        
        print("LINE 28")
        return serializer.data