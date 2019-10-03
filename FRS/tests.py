import json
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from web.settings import REST_FRAMEWORK
from django.contrib.auth.models import User


class AccountsTestCase(APITestCase):

    def setUp(self):
        self.create_url = reverse('account-create')
        self.client = APIClient()

    def test_create_user(self):
        data = {
            "username": "admin",
            "email": "admin@t.com",
            "password": "1234test"
        }
        response = self.client.post("/api/v1/users/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class FlightTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.response = self.client.post(
            '/api/v1/login/', "username=test&password=1234test", content_type="application/x-www-form-urlencoded")
        self.access_token = self.response.json()['token']

        self.json = {
            "name": "iranair",
            "number": "23",
            "scheduled_date": "2019-12-10 10:10:10",
            "departure": "tehran",
            "destination": "hong kong",
            "fare": "200"
        }

    def test_post(self):
        headers = {
            'HTTP_AUTHORIZATION': "Bearer "+self.access_token,
        }
        response = self.client.post(
            '/api/v1/flights/', data=self.json, **headers)
        self.assertEqual(response.status_code, 201)


class FlightDetailTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.response = self.client.post(
            '/api/v1/login/', "username=test&password=1234test", content_type="application/x-www-form-urlencoded")
        self.access_token = self.response.json()['token']

        self.json = {
            "name": "iranair",
            "number": "23",
            "scheduled_date": "2019-12-10T10:19",
            "departure": "tehran",
            "destination": "hong kong",
            "fare": "200"
        }

    def test_put(self):
        headers = {
            'HTTP_AUTHORIZATION': "Bearer "+self.access_token,
        }
        response = self.client.post(
            '/api/v1/flights/4/', self.json, format="json", **headers)
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        headers = {
            'HTTP_AUTHORIZATION': "Bearer "+self.access_token,
        }
        response = self.client.delete(
            '/api/v1/flights/5/', self.json, format="json", **headers)
        self.assertEqual(response.status_code, 200)
