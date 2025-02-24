from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from user_account.models import User
from ..serializers import UserSerializer
from ..permissions import OwnerPermission, UserPermission


class UserList(ListAPIView):
    queryset = User.objects.filter(is_staff=False)
    serializer_class = UserSerializer


class UserDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser, UserPermission)
    queryset = User.objects.filter(is_staff=False)
    serializer_class = UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (UserPermission, IsAdminUser)
    queryset = User.objects.filter(is_staff=False)
    serializer_class = UserSerializer
