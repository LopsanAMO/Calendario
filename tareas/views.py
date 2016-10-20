from django.shortcuts import render
from django.views.generic import View
from .forms import TareaForm, AlarmaForm, HoraForm, CompaForm

class Materia(View):
    def get(self, request):
        template_name = 'mateia'
        tarea = TareaForm()
        alarma = AlarmaForm()
        hora = HoraForm()
        compa = CompaForm()
        context = {
            'tarea': tarea,
            'alarma': alarma,
            'hora': hora,
            'compa': compa
        }
        return render(request, template_name, context)

    def post(self, request):
        action = request.POST.get('action')
        if action == 'crear':
            print('aqui va una funcion para crear una tarea')
        elif action == 'modificar':
            print('aqui va una funcion para modificar una tarea')
        elif action == 'eliminar':
            print('aqui va una funcion para eliminar una tarea')
        else:
            return redirect('/')
