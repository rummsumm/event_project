"""
PROJEKT URLs

"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("admin/", admin.site.urls),  # http://127.0.0.1:8000/admin
    # http://127.0.0.1:8000/events/hello
    # http://127.0.0.1:8000/events/show
    path("events/", include("events.urls")),
    # kleinen Schönfheitsfehler beheben: falls User schon eingloggt ist,
    # soll er auf die LOGIN_REDIRECT_URL weitergleitet werden.
    path(
        "accounts/login/",
        auth_views.LoginView.as_view(redirect_authenticated_user=True),
        name="login",
    ),
    path("accounts/", include("django.contrib.auth.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
