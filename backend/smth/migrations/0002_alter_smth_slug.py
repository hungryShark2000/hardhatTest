# Generated by Django 4.1.4 on 2023-01-05 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smth',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
    ]
