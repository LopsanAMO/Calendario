from django.shortcuts import render
from django.views.generic import View
from .forms import TareaForm, AlarmaForm, hora_alarmaForm, CompaForm

class Materia(View):
    def get(self, request):
        template_name = 'mateia'
        tarea = TareaForm()
        alarma = AlarmaForm()
        hora = hora_alarmaForm()
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
            print('aqui va una funcion para crear una materia')
        elif action == 'modificar':
            print('aqui va una funcion para modificar una materia')
        elif action == 'eliminar':
            print('aqui va una funcion para eliminar una materia')
        else:
            return redirect('/')
