# Generated by Django 5.1 on 2024-09-01 12:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_remove_freetext_title"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="FreeText",
            new_name="Deneme",
        ),
    ]