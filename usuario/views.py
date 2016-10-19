from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import View
from .forms import RegistroForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from .models import Usuario

class Registar(View):
    def get(self, request):
        template_name = 'index.html'
        form = RegistroForm()
        context = {
            'form': form
        }
        return render

    def post(self, request):
        form = RegistroForm(request.POST)
        usu = Usuario()
        if form.is_valid():
            form.save()
            try:
                usu.user = User.object.get(request.POST.get('username'))
                usu.tipo = 'usuario'
                usu.save()
                user = authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
                login(request, user)
                return redirect('usuarios:index')
        else:
            return HttpResponseRedirect('.')
