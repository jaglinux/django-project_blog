# Generated by Django 4.2.2 on 2023-10-15 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pytorch", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pytorchjob",
            name="created_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
