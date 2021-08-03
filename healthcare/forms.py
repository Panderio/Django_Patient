from typing import AsyncGenerator
from django import forms
from django.contrib.auth.forms import UserCreationForm , UsernameField
from django.contrib.auth import get_user_model

from django.db import models
from django.db.models import fields
from django.db.models.enums import Choices
from django.forms import widgets
from matplotlib import colors
from .models import Patient, User
from io  import BytesIO
import matplotlib as pllt
import matplotlib.pyplot as plt
import base64
import seaborn as sns


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
            'date_naissance':DateInputfil(),
            'date_arret_de_travail':DateInputfil(),
            'date_demande':DateInputfil(),
            'date_début':DateInputfil(),
            'date_1ère_Consolidation':DateInputfil(),
            'date_rechute':DateInputfil(),
            'date_dernière_rechute':DateInputfil(),
            'date_dernière_consolidation':DateInputfil(),
            'date_opération':DateInputfil()
        }


class PatientSearch(forms.Form):
    char_choice= (
        ('#1','Bar Chart'),
        ('#2','Pie Chart'),
        ('#3','Line Chart'),
    )
    Bureau_CNAM     =   forms.CharField()
    médecin_conseil = forms.CharField()
    gouvernorat     = forms.CharField()
    date_demande    = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    char_type = forms.ChoiceField(choices=char_choice)
 



class CustomUserCreation(UserCreationForm):
    class Meta:
        model = User
        fields = {"username",}
        field_classes = {"username": UsernameField}



#get Graph
def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph= graph.decode('utf-8')
    buffer.close()
    return graph

def get_charts(chart_type, data, **kwargs):
    pllt.use('agg')
    fig=plt.figure(figsize=(10,4))
    if chart_type == '#1':
        #plt.bar(data['id'],data['durée_cotisation_an'])
        print("bar")
        sns.barplot(x='id',y='durée_cotisation_an',data=data)
    elif chart_type == '#2':
        print("pie")
        labels=kwargs.get('labels')
        plt.pie(data=data,x='durée_cotisation_an',labels=labels)
    elif chart_type == '#3':
        print("line")
        plt.plot(data['id'],data['durée_cotisation_an'],color='green',marker='o',linestyle='dashed')
    else:
        print("error in choosing chart type")
    plt.tight_layout
    chart=get_graph()
    return chart
