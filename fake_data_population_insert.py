import os
import django
try:
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "interview_live_coding_round.settings"
    )
    django.setup()
    from django.contrib.auth.models import User 
    from music.models import Songs
    from music.models import Playlist
except ImportError as e:
    exit(1)
import traceback
from faker import Faker

def playlist_insert(profiles):
    try:
        # user_list = []
        for profile in profiles:
            user_insert = User.objects.create_user(username=profile["mail"],email=profile["mail"],password="1234")
            print(user_insert.email)

            for i in range(10):
                playlist = Playlist.objects.create(user = user_insert,name=f"playlist {i+1}")
                print(playlist.name)

                for i in range(100):
                    fake = Faker()
                    Faker.seed(i)
                    
                    song = Songs.objects.create(playlist=playlist,name=f"Song {i+1}",author = fake.name())
                    print(song.author)

    except:
        traceback.print_exc()

if __name__ == "__main__":
    fake = Faker()
    fake_profiles = [fake.profile() for i in range(100)]
    playlist_insert(fake_profiles)