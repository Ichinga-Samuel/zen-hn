from django.contrib.sites.models import Site
from django.contrib.messages.api import success
from django.urls import path, include, reverse_lazy
from django.contrib.auth.views import (PasswordChangeView, PasswordResetView, PasswordResetDoneView,
                                       PasswordResetCompleteView, PasswordChangeDoneView)

from base.utils import BreadCrumb
from .views import UserCreateView, UserDetailView, UserUpdateView, LogoutView
from allauth.account.views import PasswordResetFromKeyDoneView
# app_name = 'user_account'
home_crumb = BreadCrumb(name="Home", url=reverse_lazy("home"))
pcd_context = {"breadcrumbs": [home_crumb], "title": "Password Change"}
prd_context = {"breadcrumbs": [home_crumb], "title": "Password Reset Done"}
prc_context = {"breadcrumbs": [home_crumb], "title": "Password Reset Complete"}
# domain = "localhost:8000" if (current_domain := Site.objects.get_current().domain) == "example.com" else current_domain
extra_email_context = {"domain": 'domain'}

# some of the urls are overridden to provide custom context and redirection urls since the default ones are not
# where they should be, this is because we are using /users/ instead of /accounts/ for the urls
# especially if the app_name is changed
urlpatterns = [
    # use absolute url to specify success_url

    # default name of the success url has been changed so we need to specify the name here
    # success_url is the url to redirect to after the password has been changed
    # it can be set to an absolute url '/users/password_change/done/'
    # but we shall use lazy reverse to get the url name
    path("password_change/", PasswordChangeView.as_view(success_url=reverse_lazy('password_changed')), name="password_change"),

    # default name of the url is password_change_done. it is changed here as an example
    path("password_change/done/", PasswordChangeDoneView.as_view(extra_context=pcd_context), name="password_changed"),

    # path("reset/<uidb64>/<token>/", PasswordResetConfirmView.as_view(success_url="/users/reset/done"), name="password_reset_confirm"),

    path("password_reset/done", PasswordResetDoneView.as_view(extra_context=prd_context), name="password_reset_done"),

    path("password_reset/", PasswordResetView.as_view(extra_email_context=extra_email_context), name="password_reset"),

    path("reset/done/", PasswordResetCompleteView.as_view(extra_context=prc_context), name="password_reset_complete"),

    path("logout/", LogoutView.as_view(), name="logout"),

    path("", include("django.contrib.auth.urls")), # authentication urls for in built auth app

    path("profile/<slug:slug>/", UserDetailView.as_view(), name="profile"),

    path("update/<slug:slug>/", UserUpdateView.as_view(), name="user_update"),

    path("signup/", UserCreateView.as_view(), name="signup")
]

# users/ is used here instead of accounts/ to avoid conflict with allauth urls
# accounts/login/ [name='login'] # template: registration/login.html
# accounts/logout/ [name='logout'] # template: registration/logged_out.html
# accounts/password_change/ [name='password_change'] template: registration/password_change_form.html
# accounts/password_change/done/ [name='password_change_done'] template: registration/password_change_done.html
# accounts/password_reset/ [name='password_reset']  template: registration/password_reset_form.html
# accounts/password_reset/done/ [name='password_reset_done'] template: registration/password_reset_done.html
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm'] template: registration/password_reset_confirm.html
# accounts/reset/done/ [name='password_reset_complete'] template: registration/password_reset_complete.html
