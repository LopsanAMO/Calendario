from django.shortcuts import render
from django.views.generic import View
from .forms import Crear, Editar

class Semestre(View):
    def get(self, request):
        template_name = 'semestre.html'
        crear = Crear()
        editar = Editar()
        context = {
            'crear': crear,
            'edit': editar
        }
        return render(request, template_name, context)

    def post(self, request):
        action = request.POST.get('action')
        if action == 'crear'
            form = Crear(request.POST)
            if form.is_valid():
                form.save()
                return redirect('semestre:seme')
            else:
                return HttpResponseRedirect('.')
        elif action == 'edit':
            form = Editar(request.POST)
            if form.is_valid():
                print('tengo que hacer una funcion para actualizar datos')
                return redirect('semestre:seme')
            else:
                return HttpResponseRedirect('.')
        else :
            return HttpResponseRedirect('.')
