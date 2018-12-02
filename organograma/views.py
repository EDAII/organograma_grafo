from django.shortcuts import render
from django.contrib.auth.models import User
from .models import No
from django.contrib.auth import login as django_login, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


def cadastro(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            no = No()
            username = request.POST['usuario']
            email = request.POST['email']
            password = request.POST['senha']
            user = User.objects.create_user(
                username=username, password=password, email=email)
            no.user = user
            no_atual = No.objects.select_related(
                'user').get(user=request.user)
            no.contador = no_atual.contador + 1
            no.save()
        return render(request, 'cadastro.html')
    else:
        return HttpResponse('não está logado!!')


def login(request):
    context = {'error': ''}
    if request.method == 'POST':
        user = authenticate(
            username=request.POST['usuario'],
            password=request.POST['senha'])
        if user is not None and user.is_active:
            django_login(request, user)
        else:
            error = 'Login inválido!'
            context = {'error': error}
    return render(request, 'login.html', context)
