# Generated by Django 3.2.5 on 2021-07-30 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('healthcare', '0005_alter_patient_expert'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='docteur',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='healthcare.userprofil'),
            preserve_default=False,
        ),
    ]
