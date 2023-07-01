"""
Dieses Modul definiert die URL-Muster für das Projekt,
indem es eingehende Anfragen den entsprechenden Ansichten zuordnet.
"""
from django.urls import path
from django.views.generic import RedirectView
from django.contrib import admin

from . import views

urlpatterns = [
    # URL-Muster für die Django-Admin-Seite
    path(r"admin/", admin.site.urls),
    # URL-Muster für die Todo-Liste, erfordert Anmeldung
    path(
        "todolist/",
        views.todo_list,
        name="todolist",
        ),
    # URL-Muster zum Erstellen eines neuen Todos, erfordert Anmeldung
    path(
        "createtodo/",
        views.create_todo,
        name="createtodo",
        ),
    # URL-Muster für die Startseite, leitet zur Todo-Liste um
    path("", RedirectView.as_view(url="todolist/")),
]
