from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    add = models.CharField(max_length=150)


class Patient(models.Model):
    civilité = (
        ('M.', 'Madame'),
        ('Mr.', 'Monsieur'),
        ('D.', 'Divorcée'),
        ('Mme.', 'Mademoiselle'),
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    civil = models.CharField(max_length=4,choices=civilité)
    matricule = models.IntegerField()
    cin = models.SmallIntegerField()
    age = models.PositiveSmallIntegerField()
    ImagePic = models.ImageField(blank=True, null=True)
    Secteur_Prof = models.TextField(blank=True, null=True)
    grade = models.TextField(blank=True, null=True)
    Date_Naissance = models.DateField(blank=True, null=True)
    B_CNAM = models.TextField(blank=True, null=True)
    date_demande = models.DateField(blank=True, null=True)
    médecin_conseil = models.CharField(max_length=100,blank=True, null=True)
    date_demande = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Expert(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
