from django import forms
from django.db.models import fields
from .models import PatientPred


class PatientPredictionForm(forms.ModelForm):
    class Meta:
        model = PatientPred
        fields = (
"Type_ACT_MLD",
"mode_début",
"lombalgies",
"sciatalgie",
"diabète",
"HTA",
"respiratoire",
"Autre_1",
"mariage",
"nombre_enfants",
"rééducation",
"age",
"état_général",
"coopérant",
"poids",
"taille",
"IMC",
"corpulence",
"ceinture_de_soutien",
"boiterie",
"déroulement_du_pas",
"droit",
"gauche",
"sur_les_talons",
"sur_les_pointes_des_pieds",
"mode",
"stabilité",
"cicatrice",
"ROT",
        )
        