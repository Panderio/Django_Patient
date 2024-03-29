# Generated by Django 3.2.5 on 2021-09-01 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0003_rename_patient_patientpred'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientpred',
            name='HTA',
            field=models.SmallIntegerField(choices=[(1, 'oui'), (0, 'non')], max_length=3),
        ),
        migrations.AlterField(
            model_name='patientpred',
            name='Type_ACT_MLD',
            field=models.SmallIntegerField(choices=[(1, 'ACT'), (0, 'MLD')], max_length=3),
        ),
        migrations.AlterField(
            model_name='patientpred',
            name='diabète',
            field=models.SmallIntegerField(choices=[(1, 'oui'), (0, 'non')], max_length=2),
        ),
        migrations.AlterField(
            model_name='patientpred',
            name='lombalgies',
            field=models.SmallIntegerField(choices=[(1, 'oui'), (0, 'non')], max_length=2),
        ),
        migrations.AlterField(
            model_name='patientpred',
            name='mode_début',
            field=models.SmallIntegerField(choices=[(1, 'brutal'), (0, 'non précisé')], max_length=11),
        ),
        migrations.AlterField(
            model_name='patientpred',
            name='sciatalgie',
            field=models.SmallIntegerField(choices=[(1, 'oui'), (0, 'non')], max_length=2),
        ),
    ]
