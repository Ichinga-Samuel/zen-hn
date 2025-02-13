from django.urls import path, include
from rest_framework.routers import SimpleRouter

from ..views.user import UserList, UserDetail, UserViewSet

router = SimpleRouter()
router.register("user", UserViewSet, basename="user")
urlpatterns = [
    path("", UserList.as_view(), name="user-list"),
    path("<str:username>/", UserDetail.as_view(lookup_field='username'), name="user-detail"),
    path("usersets/", include(router.urls)), # add for usersets
]
