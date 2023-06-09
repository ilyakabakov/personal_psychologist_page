# Generated by Django 4.2 on 2023-04-26 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
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
                ("name", models.CharField(max_length=255, verbose_name="Имя")),
                (
                    "phone",
                    models.CharField(max_length=255, verbose_name="Номер телефона"),
                ),
                ("gmt", models.CharField(max_length=128, verbose_name="Часовой пояс")),
                ("query", models.TextField(verbose_name="Запрос")),
            ],
        ),
    ]
