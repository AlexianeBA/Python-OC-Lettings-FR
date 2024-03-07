from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", admin.site.urls),
    path("profiles/", include("profiles.urls")),
    path("lettings/", include("lettings.urls")),
    path("error/404/", views.handler404, name="404"),
    path("error/500/", views.handler500, name="500"),
]
