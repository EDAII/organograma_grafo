from django.urls import path
from . import views

app_name = 'organograma'
urlpatterns = [
    path('login/', views.login),
    path('cadastro/', views.cadastro),
]
