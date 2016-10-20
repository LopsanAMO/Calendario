from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import *

class ExamenView(View):
	def get(self, request):
		template_name = 'examen.html'
		examen = ExamenForm()
		alarma = AlarmaForm()
		hora = HoraForm()
		context = {
			'exaform': examen,
			'alarmaform': alarma,
			'horaform': hora
		}
		return render(request, template_name, context)

	def post(self, request):
		action = request.POST.get('action')
		if action == 'crear':
			print('aqui va una funcion para registar un examen')
		elif action == 'modificar':
			print('aqui va una funcion para editar algo de un examen ya hecho')
		elif action == 'eliminar':
			print('aqui va una funcion para eliminar una examen ya creado')
		else:
			return redirect('/')