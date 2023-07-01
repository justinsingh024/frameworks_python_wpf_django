from dataclasses import fields
from django import forms
from .models import ToDoItem

class ToDoForm(forms.ModelForm):
    """
    Ein ModelForm für das ToDoItem-Modell.
    Dieses Formular ermöglicht es, ein neues ToDoItem zu erstellen oder ein bestehendes zu bearbeiten.
    """
    class Meta:
        # Das Modell, für das dieses Formular erstellt wird
        model = ToDoItem
        # Die Felder, die im Formular angezeigt werden sollen
        fields = "__all__"