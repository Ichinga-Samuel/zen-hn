from django.urls import path

from .views import UserCreateView, UserDetailView, UserUpdateView


urlpatterns = [
    path("signup/", UserCreateView.as_view(), name="signup")
]
