from django import forms
from .models import Inscriptions

class InscriptionsForm(forms.ModelForm):
    class Meta:
        model = Inscriptions
        fields = '__all__'
