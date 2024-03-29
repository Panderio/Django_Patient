# Generated by Django 3.2.5 on 2021-07-29 00:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('healthcare', '0002_alter_patient_mode_début'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='expert',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='healthcare.expert'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='UserProfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='expert',
            name='docteur',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='healthcare.userprofil'),
            preserve_default=False,
        ),
    ]
