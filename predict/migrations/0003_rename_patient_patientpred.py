# Generated by Django 3.2.5 on 2021-08-31 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0002_auto_20210831_2329'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Patient',
            new_name='PatientPred',
        ),
    ]
