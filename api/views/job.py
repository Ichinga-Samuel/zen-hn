from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from job.models import Job
from ..serializers import JobSerializer
from ..permissions import OwnerPermission


class JobList(ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (OwnerPermission,)
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobViewSet(viewsets.ModelViewSet):
    permission_classes = (OwnerPermission,)
    queryset = Job.objects.all()
    serializer_class = JobSerializer
