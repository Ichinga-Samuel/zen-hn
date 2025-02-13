from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets

from poll.models import Poll

from ..serializers import PollSerializer
from ..permissions import OwnerPermission


class PollList(ListAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class PollDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (OwnerPermission,)
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class PollViewSet(viewsets.ModelViewSet):
    permission_classes = (OwnerPermission,)
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
