# Generated by Django 3.2.5 on 2021-07-31 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthcare', '0012_alter_patient_type_act_mld'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='carte_handicapé',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='cin',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
