# Generated by Django 4.2.7 on 2023-11-12 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quote", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="quote",
            name="quote_author",
            field=models.CharField(max_length=60),
        ),
    ]