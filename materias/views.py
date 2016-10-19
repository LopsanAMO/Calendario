from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import MateriaForm, HoraForm

class Materia(View):
    def get(self, request):
        template_name = 'materia.html'
        materia = MateriaForm()
        hora = HoraForm()
        context = {
            'materia': materia,
            'hora': HoraForm
        }
        return render(request, template_name, context)

    def post(self, request):
        if action == 'crear':
            print('aqui va una funcion para guardar materias')
        elif action == 'modificar':
            print('aqui va una funcion para modificar materias')
        elif action == 'elminar':
            print('aqui va una funcion para eliminar materias')
        else:
            return redirect('/')
        
