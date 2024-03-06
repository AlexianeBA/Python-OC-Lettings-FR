from django.urls import path
from . import views

app_name = "profiles"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:letting_id>/", views.profile, name="detail"),
]
