# Generated by Django 4.2 on 2023-04-28 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("personalpage", "0007_pricespagecontent_text_3"),
    ]

    operations = [
        migrations.AlterField(
            model_name="service",
            name="duration",
            field=models.CharField(
                help_text="Сколько по времени длится сессия",
                max_length=64,
                verbose_name="Продолжительность",
            ),
        ),
    ]