from django.urls import path
from . import views

app_name = 'fichasmedicas'

urlpatterns = [
    path('listar/', views.listar_fichasmedicas, name='listar_fichasmedicas'),
    path('adicionar/', views.adicionar_fichamedica, name='adicionar_fichamedica'),
    path('editar/<int:id_fichamedica>/', views.editar_fichamedica, name='editar_fichamedica'),
    path('excluir/<int:id_fichamedica>/', views.deletar_fichamedica, name='deletar_fichamedica'),
]
