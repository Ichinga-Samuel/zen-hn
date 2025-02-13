from django.utils.timezone import now
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from story.models import Story


class StoryTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        cls.user = User.objects.create(username="test", email="testuser@user.com")
        cls.user.set_password("testpassword")
        cls.story = Story.objects.create(
            item_id=1,
            title="Test Story",
            url="https://www.example.com",
            score=1,
            text="Test Story Text",
            by=cls.user,
            time=now(),
        )
        cls.ask_story = Story.objects.create(
            item_id=2,
            title="Ask HN: Test Story",
            url="https://www.example.com",
            score=2,
            text="Test Story Text 2",
            by=cls.user,
            time=now(),
        )

        cls.show_story = Story.objects.create(
            item_id=3,
            title="Show HN: Test Story",
            url="https://www.example.com",
            score=3,
            text="Test Story Text 3",
            by=cls.user,
            time=now(),
        )

    def test_view_stories(self):
        url = reverse("story-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.story)

    def test_view_show_stories(self):
        url = reverse("show-story-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.show_story)

    def test_view_ask_stories(self):
        url = reverse("ask-story-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.ask_story)
