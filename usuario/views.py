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
        return render(request, template_name, context)

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
                return redirect('usuario:index')
            except:
                return HttpResponseRedirect('.')
        else:
            return HttpResponseRedirect('.')

class Login(View):
    def get(self, request):
        template_name = 'login.html'
        form = LoginForm()
        context = {
            'form': form
        }
        return render(request, template_name, context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
            if user is not None:
                login(request, user)
                return redirect('usuario:calendario')
            else:
                return HttpResponseRedirect('.')
        else:
            return HttpResponseRedirect('.')

class Index(View):
    def get(self, request):
        template_name = 'index.html'
        registro = RegistroForm()
        login = LoginForm()
        context = {
            'r_form': registro,
            'l_form': login,
        }
        return render(request, template_name, context)

    def post(self, request):
        action = request.POST.get('action')
        if action == 'registro':
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
                    return redirect('usuario:index')
                except:
                    return HttpResponseRedirect('.')
            else:
                return HttpResponseRedirect('.')
        elif action == 'login':
            form = LoginForm(request.POST)
            if form.is_valid():
                user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
                if user is not None:
                    login(request, user)
                    return redirect('usuario:calendario')
                else:
                    return HttpResponseRedirect('.')
            else:
                return HttpResponseRedirect('.')
        else:
            return HttpResponseRedirect('.')
