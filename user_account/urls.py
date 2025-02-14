from django.urls import path


from .views import UserCreateView, UserDetailView, UserUpdateView

app_name = 'user_account'

urlpatterns = [
    path("signup/", UserCreateView.as_view(), name="signup")
]
