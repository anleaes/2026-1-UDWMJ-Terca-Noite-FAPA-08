from django.urls import path
from . import views

app_name = 'nutricionistas'

urlpatterns = [
    path('listar/', views.listar_nutricionistas, name='listar_nutricionistas'),
    path('adicionar/', views.adicionar_nutricionista, name='adicionar_nutricionista'),
    path('editar/<int:id_nutricionista>/', views.editar_nutricionista, name='editar_nutricionista'),
    path('excluir/<int:id_nutricionista>/', views.deletar_nutricionista, name='deletar_nutricionista'),
]
