"""
URL configuration for HackerNews project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("", include("home.urls")),
    path("users/", include("user_account.urls")),
    path("accounts/", include("allauth.urls"))
]

# Serving media files in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# django-allauth provides a set of URLs for authentication, registration, password reset, etc.
# /accounts/login/ - Login  - login.html
# /accounts/logout/ - Logout - logout.html
# /accounts/signup/ - Signup - signup.html
# /accounts/password/change/ - Password change - password_change_form.html
# /accounts/password/reset/ - Password reset - password_reset_form.html
# /accounts/password/reset/done/ - Password reset done - password_reset_done.html
