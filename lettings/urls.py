from django.urls import path
from . import views

app_name = "lettings"

urlpatterns = [
    path("", views.index, name="letting"),
    path("<int:letting_id>/", views.letting, name="letting"),
]
