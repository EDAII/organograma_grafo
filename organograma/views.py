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
            user_atual = request.user
            no_atual = No.objects.select_related(
                'user').get(user=request.user)
            no.contador = no_atual.contador + 1
            no.last_user = user_atual.username
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


def exibicao(request):
    no = []
    for user in User.objects.all():
        head = user.username
        aux = No.objects.filter(last_user=head).select_related(
            'user')
        no.append([head, aux])
    context = {'no': no}
    return render(request, 'exibicao.html', context)


def topologica(request):
    aux = No.objects.filter(last_user=None).select_related('user')
    c = 1
    lista = [[c, aux]]
    while True:
        aux = No.objects.filter(last_user=aux).select_related('user')
        c += 1
        lista.append([c, aux])
        if aux == lista[-2, 1]:
            break
    context = {'no': lista}
    return render(request, 'topologica.html', context)
