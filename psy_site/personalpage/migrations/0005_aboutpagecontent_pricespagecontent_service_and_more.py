# Generated by Django 4.2 on 2023-04-28 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("personalpage", "0004_homepagecontent_delete_textcontainer"),
    ]

    operations = [
        migrations.CreateModel(
            name="AboutPageContent",
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
                (
                    "name",
                    models.CharField(max_length=128, verbose_name="Название страницы"),
                ),
                (
                    "title",
                    models.CharField(
                        default=None,
                        max_length=255,
                        verbose_name="Главный заголовок h1",
                    ),
                ),
                ("text", models.TextField(verbose_name="Контент")),
            ],
            options={"verbose_name": "Обо мне", "verbose_name_plural": "Обо мне",},
        ),
        migrations.CreateModel(
            name="PricesPageContent",
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
                (
                    "name",
                    models.CharField(max_length=128, verbose_name="Название страницы"),
                ),
                (
                    "title",
                    models.CharField(
                        default=None,
                        max_length=255,
                        verbose_name="Главный заголовок h1",
                    ),
                ),
                ("text", models.TextField(verbose_name="Контент")),
            ],
            options={"verbose_name": "Цены", "verbose_name_plural": "Цены",},
        ),
        migrations.CreateModel(
            name="Service",
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
                (
                    "service",
                    models.CharField(
                        help_text="Введите наименование услуги",
                        max_length=128,
                        verbose_name="Услуга",
                    ),
                ),
                (
                    "duration",
                    models.CharField(
                        blank=True,
                        help_text="Сколько по времени длится сессия",
                        max_length=64,
                        verbose_name="Продолжительность",
                    ),
                ),
                (
                    "price",
                    models.IntegerField(
                        help_text="Введите цену. Числом, без букв. Не может быть пустым!",
                        verbose_name="Цена",
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="homepagecontent",
            name="title",
            field=models.CharField(
                default=None, max_length=255, verbose_name="Главный заголовок h1"
            ),
        ),
    ]
