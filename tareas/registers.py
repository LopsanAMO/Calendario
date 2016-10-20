from .models import *

def guardar_hora(hora, fecha, alarma):


def crear_tarea(request):
	materia = request.POST.get('materia')
	tarea = Tarea()
	alarma = Alarma()
	hora = Hora()
	compa = Compa()
	try:
		tarea.materia = materia
		tarea.nombre = request.POST.get('nombre')
		tarea.fecha_entrega = request.POST.get('fecha')
		tarea.prioridad = request.POST.get('prioridad')
		tarea.descripcion = request.POST.get('descripcion')
		tarea.save()
	except Exception as e:
		print(e)
		print(type(e))
	try:
		alarma.nombre = request.POST.get('nombre_alarma')
		alarma.tarea = Tarea.objects,get(nombre=request.POST.get('nombre'))
		alarma.save()
	except Exception as e:
		print(e)
		print(type(e))
	try:
		veces = request.POST.get('repetir')
		alarma = Alarma.objects.get(nombre=request.POST.get('nombre_alarma'))
		for i in range(len(veces)):
			guardar_hora(request.POST.get('hora'), request.POST.get('fecha'), alarma)
	except Exception as e:
		print(e)
		print(type(e))
	