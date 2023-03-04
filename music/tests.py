import json

from django.test import TestCase
import requests

# Create your tests here.


class APIRoutesTest(TestCase):
    def setUp(self):
        self.client = requests
        self.host = 'http://127.0.0.1:8000'

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
        response = self.client.get(self.host + '/users')

        self.assertEqual(response.status_code, 200)

    def test_total_users(self):
        response = self.client.get(self.host + '/users')

        json_response = response.json()

        self.assertTrue('total_playlists_count' in json_response['data'][0])

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
        response = self.client.get(self.host + '/playlists')

        self.assertEqual(response.status_code, 200)

    def test_total_playlist(self):
        response = self.client.get(self.host + '/playlists')

        json_response = response.json()

        self.assertTrue('total_songs_count' in json_response['data'][0])

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
        response = self.client.get(self.host + '/songs')

        self.assertEqual(response.status_code, 200)

    def test_total_songs(self):
        response = self.client.get(self.host + '/songs')

        json_response = response.json()

        self.assertTrue('playlist' in json_response['data'][0])

    def test_total_songs_user(self):
        response = self.client.get(self.host + '/songs')

        json_response = response.json()

        self.assertTrue('user' in json_response['data'][0]['playlist'])
