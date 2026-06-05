from django.urls import path
from . import views

app_name = 'categoriasalimentos'

urlpatterns = [
    path('listar/', views.listar_categoriasalimentos, name='listar_categoriasalimentos'),
    path('adicionar/', views.adicionar_categoriaalimento, name='adicionar_categoriaalimento'),
    path('editar/<int:id_categoriaalimento>/', views.editar_categoriaalimento, name='editar_categoriaalimento'),
    path('deletar/<int:id_categoriaalimento>/', views.deletar_categoriaalimento, name='deletar_categoriaalimento'),
]