# Generated by Django 4.2.5 on 2024-02-15 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("survey", "0003_client_image_client_imagemobile_client_link_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="singlepage",
            name="title",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="survey.client",
            ),
        ),
    ]
