from rest_framework import generics, permissions
from rest_framework import viewsets

from story.models import Story
from ..serializers import StorySerializer
from ..permissions import OwnerPermission


class StoryList(generics.ListAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer


class ShowStoryList(generics.ListAPIView):
    queryset = Story.objects.filter(title__startswith='Show HN:')
    serializer_class = StorySerializer


class AskStoryList(generics.ListAPIView):
    queryset = Story.objects.filter(title__startswith='Ask HN:')
    serializer_class = StorySerializer


class StoryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (OwnerPermission,)
    queryset = Story.objects.all()
    serializer_class = StorySerializer


class StoryViewSet(viewsets.ModelViewSet):
    permission_classes = (OwnerPermission,)
    queryset = Story.objects.all()
    serializer_class = StorySerializer
