from django.test import Client
from django.test import TestCase
from rest_framework import status


class DummyViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_should_dummy_view_response(self):
        # Given:
        # When: api/dummies로 api 요청을 한다
        response = self.client.get('/api/dummies')

        # Then: response.body로 {'message': 'dumb response!!'}를 받는다.
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(response.data['message'], 'dumb response!!')
