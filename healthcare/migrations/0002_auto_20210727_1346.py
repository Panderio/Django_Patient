# Generated by Django 3.2.5 on 2021-07-27 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthcare', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='Problem',
        ),
        migrations.AlterField(
            model_name='patient',
            name='B_CNAM',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Date_Naissance',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Secteur_Prof',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_demande',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='grade',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='médecin_conseil',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
