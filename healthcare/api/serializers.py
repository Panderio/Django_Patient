from rest_framework import serializers
from healthcare.models import Patient


class PatientModelSeria(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields =[
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
            'ImagePic']

