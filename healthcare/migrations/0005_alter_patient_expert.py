# Generated by Django 3.2.5 on 2021-07-29 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('healthcare', '0004_auto_20210729_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='expert',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='healthcare.expert'),
        ),
    ]
