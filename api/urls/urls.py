from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path("users/", include("api.urls.user")),
    path("polls/", include("api.urls.poll")),
    path("jobs/", include("api.urls.job")),
    path("stories/", include("api.urls.story")),
    path("api-auth/", include("rest_framework.urls")), # add for authentication with browsable API
    path("dj-rest-auth/", include("dj_rest_auth.urls")), # add for authentication with jwt
    path("dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")), # add for registration with jwt
    # add for dynamic schema generation
    # schema file is automatically generated at /api/schema and downloaded as schema.yml
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("schema/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"),
]
