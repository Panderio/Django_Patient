from django import forms
from django.db.models import fields 
from healthcare.models import Expert

class ExpertModelForm(forms.ModelForm):
    class Meta:
        model=Expert
        fields=(
            'user',
        )