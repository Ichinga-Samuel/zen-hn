from django.urls import path, include
from rest_framework.routers import SimpleRouter

from ..views.job import JobList, JobDetail, JobViewSet

router = SimpleRouter()
router.register("job", JobViewSet, basename='job') # basename is optional
urlpatterns = [
    path("", JobList.as_view(), name="job-list"),
    path("generic/<int:pk>/", JobDetail.as_view(), name="job-detail"),
    path("viewset/", include(router.urls)), # add for jobsets
]
