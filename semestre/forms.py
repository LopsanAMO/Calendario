from django import forms
from semestre.models import Semestre

class Crear(forms.ModelForm):
    class Meta:
        model = Semestre
        fields = '__all__'

class Editar(forms.ModelForm):
    class Meta:
        model = Semestre
        field = ('nombre', 'inicio', 'fin')
