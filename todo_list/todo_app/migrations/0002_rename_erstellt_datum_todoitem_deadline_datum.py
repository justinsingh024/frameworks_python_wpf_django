# Generated by Django 4.2.2 on 2023-06-25 15:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("todo_app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="todoitem",
            old_name="erstellt_datum",
            new_name="deadline_datum",
        ),
    ]
