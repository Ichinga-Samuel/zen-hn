from django.urls import path, include
from rest_framework.routers import SimpleRouter

from ..views.poll import PollList, PollDetail, PollViewSet

router = SimpleRouter()
router.register("poll", PollViewSet, basename="poll")
urlpatterns = [
    path("", PollList.as_view(), name="poll-list"),
    path("<int:pk>/", PollDetail.as_view(), name="poll-detail"),
    path("pollsets/", include(router.urls)), # add for pollsets
]
urlpatterns += router.urls
