from django import forms
from .models import *

class ExamenForm(forms.ModelForm):
	class Meta:
		model = Examen
		fields = '__all__'

class AlarmaForm(forms.ModelForm):
	class Meta:
		model = Alarma
		fields = '__all__'

class HoraForm(forms.ModelForm):
	class Meta:
		model = Hora
		fields = '__all__'