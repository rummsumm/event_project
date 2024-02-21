"""
PROJEKT URLs

"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),  # http://127.0.0.1:8000/admin

    # http://127.0.0.1:8000/events/hello
    # http://127.0.0.1:8000/events/show
    path("events/", include("events.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns