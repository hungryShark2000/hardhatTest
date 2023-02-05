# Generated by Django 4.1.5 on 2023-01-27 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("smth", "0002_alter_smth_slug"),
    ]

    operations = [
        migrations.CreateModel(
            name="FormData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("chosenSubject", models.CharField(max_length=100)),
                ("chosenYear", models.IntegerField()),
                ("chosenVersion", models.IntegerField()),
                ("chosenProblemNumber", models.IntegerField()),
                ("chosenDifficulty", models.CharField(max_length=100)),
                ("chosenTopics", models.TextField()),
            ],
        ),
    ]
