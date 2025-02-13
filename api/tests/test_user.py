from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status

from user_account.models import User


class UserListTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='testuser', email="test@user.com")
        cls.user.set_password('testpassword')

    def test_view_jobs(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.user)
