from django import forms
from .models import Materia, Horas

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = '__all__'

class HoraForm(forms.ModelForm):
    class Meta:
        model = Horas
        fields = '__all__'
