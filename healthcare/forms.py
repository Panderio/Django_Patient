from typing import AsyncGenerator
from django import forms
from django.contrib.auth.forms import UserCreationForm , UsernameField
from django.contrib.auth import get_user_model

from django.db import models
from django.db.models import fields
from django.forms import widgets
from .models import Patient, User

User = get_user_model()

class DateInputfil(forms.DateInput):
    input_type= "date"

class PatientModelForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields =(
            'date_expertise',
            'Bureau_CNAM',
            'médecin_conseil',
            'date_demande',
            'civil',
            'first_name',
            'last_name',
            'matricule',
            'secteur_professionnel',
            'grade',
            'adresse_délégation',
            'gouvernorat',
            'date_naissance',
            'lieu_naissance',
            'cin',
            'carte_handicapé',
            'handicap',
            'date_arret_de_travail',
            'Type_ACT_MLD',
            'mode_début',
            'date_début',
            'date_1ère_Consolidation',
            'date_rechute',
            'date_dernière_rechute',
            'date_dernière_consolidation',
            'mécanisme',
            'lombalgies',
            'sciatalgie',
            'diabète',
            'HTA',
            'respiratoire',
            'Autre',
            'Autre_1',
            'mariage',
            'nombre_enfants',
            'durée_cotisation_an',
            'dernier_emploi',
            'scolarisation',
            'plainte',
            'Pb_sphinctérien',
            'rééducation',
            'état_général',
            'coopérant',
            'poids',
            'taille',
            'IMC',
            'corpulence',
            'ceinture_de_soutien',
            'boiterie',
            'déroulement_du_pas',
            'droit',
            'gauche',
            'sur_les_talons',
            'sur_les_pointes_des_pieds',
            'mode',
            'stabilité',
            'indice_de_schober',
            'distance_doigts_sol',
            'lordose_lombaire',
            'droit_1',
            'gauche_1',
            'cicatrice',
            'date_opération',
            'type_opération',
            'ROT',
            'canal_étroit',
            'état_discal',
            'L3_L4',
            'L4_L5',
            'L5_S1',
            'malformation',
            'repos',
            'reprise',
            'mise_en_Invalidité',
            'Comments1',
            'Comments2',
            'age',
            'ImagePic',
        )
        widgets = {
            'date_expertise':DateInputfil(),
            'date_demande':DateInputfil(),
            'date_début':DateInputfil(),
            'date_1ère_Consolidation':DateInputfil(),
            'date_rechute':DateInputfil(),
            'date_dernière_rechute':DateInputfil(),
            'date_dernière_consolidation':DateInputfil()
        }


class PatientForm(forms.Form):
    civilité = (
        ('M.', 'Madame'),
        ('Mr.', 'Monsieur'),
        ('D.', 'Divorcée'),
        ('Mme.', 'Mademoiselle'),
    )
    first_name = forms.CharField()
    last_name = forms.CharField()
    civil = forms.ChoiceField(choices=civilité)
    matricule = forms.IntegerField(min_value=0)
    cin = forms.IntegerField(min_value=0)
    age = forms.IntegerField(min_value=0)

class CustomUserCreation(UserCreationForm):
    class Meta:
        model = User
        fields = {"username",}
        field_classes = {"username": UsernameField}