# Generated by Django 3.0.8 on 2020-09-29 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inference_modules", "0002_inferencemodule_is_gpu"),
    ]

    operations = [
        migrations.AlterField(
            model_name="inferencemodule",
            name="is_gpu",
            field=models.BooleanField(default=False),
        ),
    ]