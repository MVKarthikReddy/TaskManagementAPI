# Generated by Django 4.2.1 on 2023-10-08 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_task_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="user",
            new_name="user_id",
        ),
    ]