from django.urls import path

from . import views

app_name = "tasks_app"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>/", views.details, name="details"),
    path("create/", views.create, name="create"),
    path("edit/<int:id>", views.edit, name="edit")
]
