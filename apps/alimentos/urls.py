from django.urls import path
from . import views

app_name = 'alimentos'

urlpatterns = [
    path('listar/', views.listar_alimentos, name='listar_alimentos'),
    path('adicionar/', views.adicionar_alimento, name='adicionar_alimento'),
    path('editar/<int:id_alimento>/', views.editar_alimento, name='editar_alimento'),
    path('deletar/<int:id_alimento>/', views.deletar_alimento, name='deletar_alimento'),
]