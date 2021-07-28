from typing import AsyncGenerator
from django import forms
from django.db.models import fields
from .models import Patient

class PatientModelForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields =(
            'first_name',
            'last_name',
            'civil',
            'matricule',
            'cin',
            'age'
        )


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