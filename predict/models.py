from django.db import models

# Create your models here.
class PatientPred(models.Model):
    TypeAM=(
        (1,'ACT'),
        (0,'MLD'),
    )
    ModeD = (
        (1,'brutal'),
        (0,'non précisé'),
    )
    status= (
        (1,'oui'),
        (0,'non'),
        (3,'divorcé(é)'),
        (4,'veuve'),
    ) 
    y_n= (
        (1,'oui'),
        (0,'non'),
    )
    respira= (
        (1,'BPCO'),
        (2,'#asthme'),
        (3,'#tuberculose'),
        (4,'#DDB'),
    )
    autr =(
        (0,'NONE'),
        (1,'#depression '),
        (2,'##hyo '),
        (3,'##pso '),
        (4,'##vit '),
        (5,'#ary'),
        (6,'#osté'),
    )
    etatgen = (
        (1,"bon"),
        (0,"moyen")
    )
    coper = (
        (1,"oui"),
        (0,"non"),
        (2,"peu")
    )
    boitr = (
        (0,"non"),
        (1,"Bil"),
        (2,"gauche"),
        (3,"droit")
    )
    deroulmpas = (
        (1,"complet"),
        (0,"incomplet")
    )
    drt = (
    (1,"#stable"),
    (0,"#instable"),
    (2,"#gene")
    )
    
    gach = (
    (1,"#stable"),
    (0,"#instable"),
    (2,"#gene")
    )    
    talon = (
    (1,"#pos"),
    (0,"#instable"),
    (2,"#gene"),
    (3,"#impossible"),
    )
    pieds= (
    (1,"#pos"),
    (0,"#instable"),
    (2,"#gene"),
    (3,"#impossible"),
    )
    mod = (
    (1,"#complet"),
    (0,"#incomplet"),
    (2,"#impossible"),
    )
    corp= (
        (1,"normale"),
        (2,"obésité modérée"),
        (3,"surpoids"),
        (4,"obésité sévère"),
        (5,"maigre"),
        (6,"obésité morbide"),
        (7,"insuffisance pondérale")
    )

    stab = (
    (1,"#stable"),
    (0,"#instable"),
    (2,"#gene"),
    (3,"#impossible")
    ) 

    sciatlg = (
        (1,"oui"),
        (0,"non"),
        (2,"bilatérale"),
        (3,"gauche"),
        (4,"droite"),
    )

    rott = (
        (1,"normaux"),
        (2,"rotuiliens abolis achilééens normaux"),
        (3,"rotuliens abolis"),
        (4,"abolis à gauche"),
        (5,"rotulien droit aboli")
    )

    Type_ACT_MLD=models.SmallIntegerField(choices=TypeAM)
    mode_début=models.SmallIntegerField(choices=ModeD)
    lombalgies=models.SmallIntegerField(choices=y_n)
    sciatalgie=models.SmallIntegerField(choices=y_n)
    diabète=models.SmallIntegerField(choices=y_n)
    HTA=models.SmallIntegerField(choices=y_n)
    respiratoire=models.PositiveSmallIntegerField(choices=respira)
    Autre_1=models.PositiveSmallIntegerField(choices=autr)
    mariage=models.PositiveSmallIntegerField(choices=status)
    nombre_enfants=models.PositiveSmallIntegerField(blank=True, null=True)
    rééducation=models.PositiveSmallIntegerField( choices=y_n)
    age = models.PositiveSmallIntegerField()
    état_général=models.PositiveSmallIntegerField( choices=etatgen)
    coopérant=models.PositiveSmallIntegerField( choices=coper)
    poids =models.PositiveSmallIntegerField()
    taille=models.PositiveSmallIntegerField()
    IMC=models.FloatField()
    corpulence=models.PositiveSmallIntegerField( choices=corp)
    ceinture_de_soutien=models.PositiveSmallIntegerField(choices=y_n)
    boiterie=models.PositiveSmallIntegerField(choices=boitr)
    déroulement_du_pas=models.PositiveSmallIntegerField(choices=deroulmpas)
    droit=models.PositiveSmallIntegerField(choices=drt)
    gauche=models.PositiveSmallIntegerField( choices=gach)
    sur_les_talons=models.PositiveSmallIntegerField(choices=talon)
    sur_les_pointes_des_pieds=models.PositiveSmallIntegerField(choices=pieds)
    mode=models.PositiveSmallIntegerField( choices=mod)
    stabilité=models.PositiveSmallIntegerField( choices=stab)
    cicatrice=models.PositiveSmallIntegerField(choices=y_n)
    ROT=models.PositiveSmallIntegerField(choices=rott)
    