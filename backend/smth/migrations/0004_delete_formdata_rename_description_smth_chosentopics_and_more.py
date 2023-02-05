# Generated by Django 4.1.5 on 2023-01-27 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("smth", "0003_formdata"),
    ]

    operations = [
        migrations.DeleteModel(name="FormData",),
        migrations.RenameField(
            model_name="smth", old_name="description", new_name="chosenTopics",
        ),
        migrations.RemoveField(model_name="smth", name="slug",),
        migrations.RemoveField(model_name="smth", name="title",),
        migrations.AddField(
            model_name="smth",
            name="chosenDifficulty",
            field=models.CharField(default="None", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="smth",
            name="chosenProblemNumber",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="smth",
            name="chosenSubject",
            field=models.CharField(default="None", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="smth",
            name="chosenVersion",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="smth",
            name="chosenYear",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]