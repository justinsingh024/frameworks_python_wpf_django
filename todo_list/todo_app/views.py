"""
Dieses Modul enthält Ansichten für die Todo-App.
Es enthält Ansichten zum Anzeigen einer Todo-Liste, zum Erstellen neuer Todos
 und zum Abmelden.
"""

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse


from .forms import ToDoForm

from .models import ToDoItem


@login_required(login_url='login')
def todo_list(request):
    """
    Zeigt eine Liste von ToDo-Elementen an, die noch nicht erledigt sind.
    Wenn die Anfrage POST ist, wird das erledigte
    Feld des angegebenen ToDo-Elements aktualisiert.
    """
    if request.method == 'POST':
        # Hole die ID des ToDo-Elements aus den POST-Daten
        todo_id = request.POST.get('todo')
        # Hole das ToDo-Element aus der Datenbank mit der ID
        todo = ToDoItem.objects.get(id=todo_id)
        # Aktualisiere das erledigte Feld des ToDo-Elements
        todo.fertig = not todo.fertig
        # Speichere das aktualisierte ToDo-Element in der Datenbank
        todo.save()
        # Leite den Benutzer auf die Todo-Liste um
        return redirect('todolist')

    # Hole alle ToDo-Elemente aus der Datenbank, die noch nicht erledigt sind
    todo_list_ = ToDoItem.objects.filter(fertig=False)
    # Rendere die todo_list.html-Datei mit den ToDo-Elementen
    # aus der todo_list_ Variable
    return render(request, 'todo_list.html', {'todo_list': todo_list_})


@login_required(login_url='login')
def create_todo(request):
    """
    Zeigt ein Formular zum Erstellen eines neuen ToDo-Elements an.
    Wenn die Anfrage POST ist, wird das Formular verarbeitet und das neue ToDo-Element in der Datenbank gespeichert.
    """
    context = {}
    form = ToDoForm(request.POST or None)

    if request.method == 'POST':
        # Verarbeite das Formular, speichere Daten, etc.
        # Wenn das Formular gültig ist, speichere die Daten in der Datenbank
        if form.is_valid():
            form.save()
        # Leite den Benutzer auf die Todo-Liste um
        return redirect(reverse('todolist'))
    context['form'] = form
    return render(request, 'create_form.html', context)


def logout_view(request):
    """
    Meldet den Benutzer ab und leitet ihn auf die Todo-Liste um.
    """
    logout(request)

    return redirect(reverse('todolist'))
