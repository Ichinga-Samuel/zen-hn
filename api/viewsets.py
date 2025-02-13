from rest_framework import viewsets

from job.models import Job
from story.models import Story
from poll.models import Poll
from user_account.models import User

from .serializers import *
from .permissions import OwnerPermission


class StoryViewSet(viewsets.ModelViewSet):
    permission_classes = (OwnerPermission,)
    queryset = Story.objects.all()
    serializer_class = StorySerializer


class PollViewSet(viewsets.ModelViewSet):
    permission_classes = (OwnerPermission,)
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class JobViewSet(viewsets.ModelViewSet):
    permission_classes = (OwnerPermission,)
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (OwnerPermission,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
