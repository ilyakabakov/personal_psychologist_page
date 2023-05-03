# Generated by Django 4.2 on 2023-04-26 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("personalpage", "0002_textcontainer_alter_client_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="textcontainer",
            options={
                "verbose_name": "Наполнение сайта",
                "verbose_name_plural": "Наполнение сайта",
            },
        ),
        migrations.AddField(
            model_name="textcontainer",
            name="title",
            field=models.CharField(
                default=None, max_length=255, verbose_name="Заголовок"
            ),
        ),
        migrations.AlterField(
            model_name="textcontainer",
            name="name",
            field=models.CharField(max_length=255, verbose_name="naming"),
        ),
    ]