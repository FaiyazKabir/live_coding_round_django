from django.test import TestCase, Client


# Create your tests here.


class APIRoutesTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_users(self):
        """
        Get all users list with their total playlist as an attribute in the JSON object.
        Response should be paginated.
        {
            "data": [
                {
                    "id": 1,
                    "username": "bob",
                    ...,
                    "total_playlists_count": 123
                }
            ]
        }
        """
        response = self.client.get('/users')

        self.assertEqual(response.status_code, 200)

    def test_playlists(self):
        """
        Get all playlists with their total song as an attribute and user's object in the JSON object.
        Response should be paginated.
        {
            "data": [
                {
                    "id": 1,
                    "user": {
                        "id": 1,
                        ...
                    },
                    ...,
                    "total_songs_count": 123
                }
            ]
        }
        """
        response = self.client.get('/playlists')

        self.assertEqual(response.status_code, 200)

    def test_songs(self):
        """
        Get all songs with their playlist object with related user object in the JSON object.
        Response should be paginated.
        {
            "data": [
                {
                    "id": 1,
                    "name": "don't let me down by Beatles"
                    "playlist": {
                        "id": 1,
                        "name": "my fav",
                        "user": {
                            "id": 1,
                            ...
                        }
                    },
                }
            ]
        }
        """
        response = self.client.get('/songs')

        self.assertEqual(response.status_code, 200)
