import grpc
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
# import music.account.account_pb2 as account_pb2
# import music.account.account_pb2_grpc as account_pb2_grpc
# import playlist
import music.playlist.playlist_pb2 as playlist_pb2
import music.playlist.playlist_pb2_grpc as playlist_pb2_grpc
# with grpc.insecure_channel('localhost:50051') as channel:
#     stub = account_pb2_grpc.UserControllerStub(channel)
#     for user in stub.List(account_pb2.UserListRequest()):
#         print(user, end='')


with grpc.insecure_channel('localhost:50051') as channel:
    stub = playlist_pb2_grpc.PlaylistControllerStub(channel)
    print("STUB RUNNING")
    print("*************************",playlist_pb2.PlaylistRetrieveRequest(id=2))
    playlist = stub.Retrieve(playlist_pb2.PlaylistRetrieveRequest(id=1))
    print(playlist)