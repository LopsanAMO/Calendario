from django import forms
from .models import Tarea, Alarma, Hora, Compa

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = '__all__'

class AlarmaForm(forms.ModelForm):
    class Meta:
        model = Alarma
        fields = '__all__'

class HoraForm(forms.ModelForm):
    class Meta:
        model = Hora
        fields = '__all__'

class CompaForm(forms.ModelForm):
    class Meta:
        model = Compa
        fields = '__all__'
