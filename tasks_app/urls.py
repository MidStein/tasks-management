from django.urls import path

from . import views

app_name = "tasks_app"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>/", views.details, name="details"),
    path("create/", views.create, name="create"),
    path("edit/<int:id>", views.edit, name="edit"),
    path("delete/<int:id>", views.delete, name="delete"),
    path("login-form/", views.login_form, name="login-form"),
    path("login/", views.login_user, name="login")
]
