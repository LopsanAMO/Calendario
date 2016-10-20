from .models import *
from materias.models import Materia

def guardar_hora(hora_alarma, fecha, alarma, hora):
	try:
		hora.hora = hora_alarma
		hora.fecha = fecha_entrega
		hora.alarma = alarma
		hora.save()
	except Exception as e:
		print(e)
		print(type(e))

def crear_tarea(request):
	materia = request.POST.get('materia')
	tarea = Tarea()
	alarma = Alarma()
	hora = Hora()
	compa = Compa()
	try:
		tarea.materia = materia
		tarea.nombre = request.POST.get('nombre')
		tarea.fecha_entrega = request.POST.get('fecha_entrega')
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
			guardar_hora(request.POST.get('hora'), request.POST.get('fecha'), alarma, hora)
	except Exception as e:
		print(e)
		print(type(e))

def modificar_tarea(request):
	tarea = request.POST.get('tarea')
	obj_tarea = Tarea.objects.get(id=tarea)
	try:
		if request.POST.get('nombre') == '' or None:
			pass
		else:
			obj_tarea.nombre = request.POST.get('nombre')
		if request.POST.get('fecha_entrega') == '' or None:
			pass
		else:
			obj_tarea.fecha_entrega = request.POST.get('fecha_entrega')
		if request.POST.get('prioridad') == '' or None:
			pass
		else:
			obj_tarea.prioridad = request.POST.get('prioridad')
		if request.POST.get('descripcion') == '' or None:
			pass
		else:
			obj_tarea.descripcion = request.POST.get('descripcion')
		if request.POST.get('materia') == '' or None:
			pass
		else:
			materia = request.POST.get('materia')
			obj_materia = Materia.objects.get(id=materia)
			obj_tarea.materia = materia
		try:
			obj_tarea.save()
		except Exception as e:
			print(e)
			print(type(e))
	except Exception as e:
		print(e)
		print(type(e))

	try:
		obj_alarma = Alarma.objects.get(tarea=Tarea.objects.get(id=tarea))
		try:
			if request.POST.get('nombre_alarma') == '' or None:
				pass
			else:
				obj_alarma.nombre = request.POST.get('nombre_alarma')
			obj_alarma.save()
		except Exception as e:
			print(e)
			print(type(e))
	except Exception as e:
		print(e)
		print(type(e))
	try:
		hora = Hora.objects.get(alarma=Alarma.objects.get(tarea=Tarea.objects,get(id=tarea)))
		try:
			if request.POST.get('hora') == '' or None:
				pass
			else:
				hora.hora = request.POST.get('hora')
			if request.POST.get('fecha') == '' or None:
				pass
			else:
				hora.fecha = request.POST.get('fecha')
			hora.save()
		except Exception as e:
			print(e)
			print(type(e))
	except Exception as e:
		print(e)
		print(type(e))
