from django.urls import path
from . import views

app_name = 'treinadores'

urlpatterns = [
    path('listar/', views.listar_treinadores, name='listar_treinadores'),
    path('adicionar/', views.adicionar_treinador, name='adicionar_treinador'),
    path('editar/<int:id_treinador>/', views.editar_treinador, name='editar_treinador'),
    path('excluir/<int:id_treinador>/', views.deletar_treinador, name='deletar_treinador'),
]
