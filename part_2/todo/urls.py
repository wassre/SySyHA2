from django.urls import path

from . import views

urlpatterns = [
    path("", views.todolist, name=""),
    path("impressum/", views.impressum, name="impressum"),
    path("new/", views.new, name="new"),
    path("edit/<int:id>", views.edit, name="edit"),
]
