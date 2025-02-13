from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status

from job.models import Job


class JobListTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        cls.user = User.objects.create(username='test', email="test@user.com")
        cls.job = Job.objects.create(title='test', url='https://example.com',
                           text='text', by=cls.user, item_id=1234567890, score=1)

    def test_view_jobs(self):
        url = reverse('job-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.job)
