# Generated by Django 4.2.7 on 2023-11-09 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="joboffer",
            name="available",
            field=models.BooleanField(default=True),
        ),
    ]