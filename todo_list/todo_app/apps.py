from django.apps import AppConfig


class TodoAppConfig(AppConfig):
    """
    Konfigurationsklasse für die Todo-App.
    """
    # Standard-Auto-Feldtyp für Modelle in dieser App
    default_auto_field = "django.db.models.BigAutoField"
    # Der Name dieser App
    name = "todo_app"
