"""
PROJEKT URLs
"""

from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularSwaggerView
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token

# 227de4d07191b43fe505b9f03b8d653849fc1a05

urlpatterns = [
    # http://127.0.0.1:8000
    path("", include("pages.urls")),
    path("token", obtain_auth_token, name="api-token"),  # per POST Zugangsdaten senden
    path("admin/", admin.site.urls),  # http://127.0.0.1:8000/admin
    # http://127.0.0.1:8000/events/hello
    # http://127.0.0.1:8000/events/show
    path("events/", include("events.urls")),
    path("api/events/", include("events.api.urls")),
    # kleinen Schönfheitsfehler beheben: falls User schon eingloggt ist,
    # soll er auf die LOGIN_REDIRECT_URL weitergleitet werden.
    path(
        "accounts/login/",
        auth_views.LoginView.as_view(redirect_authenticated_user=True),
        name="login",
    ),
    path("accounts/", include("django.contrib.auth.urls")),
    path(
        "schema/",
        SpectacularAPIView.as_view(api_version="v1"),
        name="schema",
    ),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
