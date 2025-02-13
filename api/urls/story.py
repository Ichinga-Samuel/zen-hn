from django.urls import path, include
from rest_framework.routers import SimpleRouter

from ..views.story import StoryList, AskStoryList, ShowStoryList, StoryDetail, StoryViewSet

routers = SimpleRouter()
routers.register("story", StoryViewSet, basename="story")
urlpatterns = [
    path("<int:pk>/", StoryDetail.as_view(), name="story-detail"),
    path("", StoryList.as_view(), name="story-list"),
    path("ask/", AskStoryList.as_view(), name="ask-story-list"),
    path("show/", ShowStoryList.as_view(), name="show-story-list"),
    path("storysets/", include(routers.urls)),
]
