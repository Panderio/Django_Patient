# Generated by Django 3.2.5 on 2021-07-30 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthcare', '0007_auto_20210730_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='durée_cotisation_an',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
