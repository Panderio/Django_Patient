# Generated by Django 3.2.5 on 2021-09-01 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0005_auto_20210902_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientpred',
            name='Autre_1',
            field=models.PositiveSmallIntegerField(choices=[(0, 'NONE'), (1, '#depression '), (2, '##hyo '), (3, '##pso '), (4, '##vit '), (5, '#ary'), (6, '#osté')]),
        ),
        migrations.AlterField(
            model_name='patientpred',
            name='ROT',
            field=models.PositiveSmallIntegerField(choices=[(1, 'normaux'), (2, 'rotuiliens abolis achilééens normaux'), (3, 'rotuliens abolis'), (4, 'abolis à gauche'), (5, 'rotulien droit aboli')]),
        ),
        migrations.AlterField(
            model_name='patientpred',
            name='boiterie',
            field=models.PositiveSmallIntegerField(choices=[(0, 'non'), (1, 'Bil'), (2, 'gauche'), (3, 'droit')]),
        ),
        migrations.AlterField(
            model_name='patientpred',
            name='ceinture_de_soutien',
            field=models.PositiveSmallIntegerField(choices=[(1, 'oui'), (0, 'non')]),
        ),
        migrations.AlterField(
            model_name='patientpred',
            name='cicatrice',
            field=models.PositiveSmallIntegerField(choices=[(1, 'oui'), (0, 'non')]),
        ),
        migrations.AlterField(
            model_name='patientpred',
            name='coopérant',
            field=models.PositiveSmallIntegerField(choices=[(1, 'oui'), (0, 'non'), (2, 'peu')]),
        ),
        migrations.AlterField(
            model_name='patientpred',
            name='corpulence',
            field=models.PositiveSmallIntegerField(choices=[(1, 'normale'), (2, 'obésité modérée'), (3, 'surpoids'), (4, 'obésité sévère'), (5, 'maigre'), (6, 'obésité morbide'), (7, 'insuffisance pondérale')]),
        ),
        migrations.AlterField(
            model_name='patientpred',
            name='droit',
            field=models.PositiveSmallIntegerField(choices=[(1, '#stable'), (0, '#instable'), (2, '#gene')]),
        ),
        migrations.AlterField(
            model_name='patientpred',
            name='déroulement_du_pas',
            field=models.PositiveSmallIntegerField(choices=[(1, 'complet'), (0, 'incomplet')]),
        ),
        migrations.AlterField(
            model_name='patientpred',
            name='gauche',
            field=models.PositiveSmallIntegerField(choices=[(1, '#stable'), (0, '#instable'), (2, '#gene')]),
        ),
        migrations.AlterField(
            model_name='patientpred',
            name='mariage',
            field=models.PositiveSmallIntegerField(choices=[(1, 'oui'), (0, 'non'), (3, 'divorcé(é)'), (4, 'veuve')]),
        ),
        migrations.AlterField(
            model_name='patientpred',
            name='mode',
            field=models.PositiveSmallIntegerField(choices=[(1, '#complet'), (0, '#incomplet'), (2, '#impossible')]),
        ),
        migrations.AlterField(
            model_name='patientpred',
            name='respiratoire',
            field=models.PositiveSmallIntegerField(choices=[(1, 'BPCO'), (2, '#asthme'), (3, '#tuberculose'), (4, '#DDB')]),
        ),
        migrations.AlterField(
            model_name='patientpred',
            name='rééducation',
            field=models.PositiveSmallIntegerField(choices=[(1, 'oui'), (0, 'non')]),
        ),
        migrations.AlterField(
            model_name='patientpred',
            name='stabilité',
            field=models.PositiveSmallIntegerField(choices=[(1, '#stable'), (0, '#instable'), (2, '#gene'), (3, '#impossible')]),
        ),
        migrations.AlterField(
            model_name='patientpred',
            name='sur_les_pointes_des_pieds',
            field=models.PositiveSmallIntegerField(choices=[(1, '#pos'), (0, '#instable'), (2, '#gene'), (3, '#impossible')]),
        ),
        migrations.AlterField(
            model_name='patientpred',
            name='sur_les_talons',
            field=models.PositiveSmallIntegerField(choices=[(1, '#pos'), (0, '#instable'), (2, '#gene'), (3, '#impossible')]),
        ),
        migrations.AlterField(
            model_name='patientpred',
            name='état_général',
            field=models.PositiveSmallIntegerField(choices=[(1, 'bon'), (0, 'moyen')]),
        ),
    ]
