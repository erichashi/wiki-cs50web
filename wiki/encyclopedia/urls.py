from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.get_entry, name="titleEntry"),
    path("new", views.create_new, name="create"),
    path("edit/<str:title>", views.edit_page, name="edit")
]
