from django.db import models

from datetime import date


class ToDoItem(models.Model):
    """
    Ein Modell, das ein ToDo-Element darstellt.
    Jedes ToDo-Element hat ein Fälligkeitsdatum, einen Namen und
    einen Status, der angibt, ob es erledigt ist oder nicht.
    """
    # Das Fälligkeitsdatum des ToDo-Elements, standardmäßig auf
    # das heutige Datum gesetzt
    deadline_datum = models.DateField(default=date.today)
    # Der Name des ToDo-Elements
    name = models.CharField(max_length=200)
    # Der Status des ToDo-Elements, standardmäßig auf nicht erledigt gesetzt
    fertig = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)
