from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.db.models.fields import CharField, IntegerField

# Create your models here.

class User(AbstractUser):
    pass
    

class UserProfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Patient(models.Model):
    civilité = (
        ('Madame', 'Madame'),
        ('Monsieur', 'Monsieur'),
        ('Divorcée', 'Divorcée'),
        ('Mademoiselle', 'Mademoiselle'),
    )
    TypeAM=(
        ('ACT','ACT'),
        ('MLD','MLD'),
    )
    ModeD = (
        ('brutal','brutal'),
        ('non précisé','non précisé'),
    )
    status= (
        ('oui','oui'),
        ('non','non'),
        ('divorcé','divorcé(é)'),
        ('veuve','veuve'),
    )
    
    y_n= (
        ('oui','oui'),
        ('non','non'),
        )
    
    date_expertise=models.DateField(("date expertise"),blank=True, null=True)
    Bureau_CNAM = models.CharField(max_length=150,blank=True, null=True)
    médecin_conseil=models.CharField(max_length=100,blank=True, null=True)
    date_demande=models.DateField(blank=True, null=True)
    civil = models.CharField(max_length=12,choices=civilité)
    first_name = models.CharField(max_length=100,blank=True, null=True)
    last_name = models.CharField(max_length=100,blank=True, null=True)
    matricule = models.CharField(max_length=150,blank=True, null=True)
    secteur_professionnel = models.CharField(max_length=150,blank=True, null=True)
    grade = models.CharField(max_length=100,blank=True, null=True)
    adresse_délégation=models.CharField(max_length=150,blank=True, null=True)
    gouvernorat=models.CharField(max_length=250,blank=True, null=True)
    date_naissance = models.DateField(blank=True, null=True)
    lieu_naissance =models.CharField(max_length=250,blank=True, null=True)
    cin = models.CharField(max_length=150,blank=True, null=True)
    carte_handicapé =CharField(max_length=250,blank=True, null=True)
    handicap=models.CharField(max_length=250,blank=True, null=True)
    date_arret_de_travail=models.DateField(blank=True, null=True)
    Type_ACT_MLD=models.CharField(max_length=3,choices=TypeAM,blank=True, null=True)
    mode_début=models.CharField(max_length=11,choices=ModeD)
    date_début=models.DateField(blank=True, null=True)
    date_1ère_Consolidation=models.DateField(blank=True, null=True)
    date_rechute=models.DateField(blank=True, null=True)
    date_dernière_rechute=models.DateField(blank=True, null=True)
    date_dernière_consolidation=models.DateField(blank=True, null=True)
    mécanisme=models.CharField(max_length=150,blank=True, null=True)
    lombalgies=models.CharField(max_length=3,default="oui")
    sciatalgie=models.CharField(max_length=13,default="non")
    diabète=models.CharField(max_length=3,default=0)
    HTA=models.CharField(max_length=3,default=0,blank=True, null=True)
    respiratoire=models.CharField(max_length=150,default=0,blank=True, null=True)
    Autre=models.CharField(max_length=250,default=0,blank=True, null=True)
    Autre_1=models.CharField(max_length=250,default=0,blank=True, null=True)
    mariage=models.CharField(max_length=7,choices=status)
    nombre_enfants=models.PositiveSmallIntegerField(blank=True, null=True)
    durée_cotisation_an=models.PositiveSmallIntegerField(blank=True, null=True)
    dernier_emploi=models.CharField(max_length=150,blank=True, null=True)
    scolarisation=models.CharField(max_length=150,blank=True, null=True)
    plainte=models.CharField(max_length=150,blank=True, null=True)
    Pb_sphinctérien=models.CharField(max_length=150,blank=True, null=True)
    rééducation=models.CharField(max_length=150,blank=True, null=True)
    état_général=models.CharField(max_length=150,blank=True, null=True)
    coopérant=models.CharField(max_length=150,blank=True, null=True)
    poids =models.CharField(max_length=150,blank=True, null=True)
    taille=models.CharField(max_length=150,blank=True, null=True)
    IMC=models.CharField(max_length=150,blank=True, null=True)
    corpulence=models.CharField(max_length=150,blank=True, null=True)
    ceinture_de_soutien=models.CharField(max_length=150,blank=True, null=True)
    boiterie=models.CharField(max_length=150,blank=True, null=True)
    déroulement_du_pas=models.CharField(max_length=150,blank=True, null=True)
    droit=models.CharField(max_length=150,blank=True, null=True)
    gauche=models.CharField(max_length=150,blank=True, null=True)
    sur_les_talons=models.CharField(max_length=150,blank=True, null=True)
    sur_les_pointes_des_pieds=models.CharField(max_length=150,blank=True, null=True)
    mode=models.CharField(max_length=150,blank=True, null=True)
    stabilité=models.CharField(max_length=150,blank=True, null=True)
    indice_de_schober=models.CharField(max_length=150,blank=True, null=True)
    distance_doigts_sol=models.CharField(max_length=150,blank=True, null=True)
    lordose_lombaire=models.CharField(max_length=150,blank=True, null=True)
    droit_1=models.CharField(max_length=150,blank=True, null=True)
    gauche_1=models.CharField(max_length=150,blank=True, null=True)
    cicatrice=models.CharField(max_length=150,blank=True, null=True)
    date_opération=models.CharField(max_length=150,blank=True, null=True)
    type_opération=models.CharField(max_length=150,blank=True, null=True)
    ROT=models.CharField(max_length=150,blank=True, null=True)
    canal_étroit=models.CharField(max_length=3,choices=y_n,blank=True, null=True)
    état_discal=models.CharField(max_length=150,blank=True, null=True)
    L3_L4=models.CharField(max_length=150,blank=True, null=True)
    L4_L5=models.CharField(max_length=150,blank=True, null=True)
    L5_S1=models.CharField(max_length=150,blank=True, null=True)
    malformation=models.CharField(max_length=150,blank=True, null=True)
    repos=models.CharField(max_length=25,blank=True, null=True)
    reprise=models.CharField(max_length=3,choices=y_n,blank=True, null=True)
    mise_en_Invalidité=models.CharField(max_length=3,choices=y_n,blank=True, null=True)
    Comments1= models.CharField(max_length=150,blank=True, null=True)
    Comments2= models.CharField(max_length=150,blank=True, null=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    ImagePic = models.ImageField(blank=True, null=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Expert(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    docteur = models.ForeignKey(UserProfil, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username
    

def post_user_created_signal(sender, instance, created, **kwargs):
    print(instance,created)
    if created:
        UserProfil.objects.create(user=instance)

post_save.connect(post_user_created_signal,sender=User)

