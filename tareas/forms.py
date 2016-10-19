from django import forms
from .models import Tarea, Alarma, hora_alarma, Compa

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = '__all__'

class AlarmaForm(forms.ModelForm):
    class Meta:
        model = Alarma
        fields = '__all__'

class hora_alarmaForm(forms.ModelForm):
    class Meta:
        model = hora_alarma
        fields = '__all__'

class CompaForm(forms.ModelForm):
    class Meta:
        model = Compa
        fields = '__all__'
