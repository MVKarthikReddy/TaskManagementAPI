# Generated by Django 4.2.1 on 2023-10-08 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_rename_user_task_user_id"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Task",
        ),
    ]