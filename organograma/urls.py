from django.urls import path
from . import views

app_name = 'organograma'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('exibicao/', views.exibicao, name='exibicao')
]
