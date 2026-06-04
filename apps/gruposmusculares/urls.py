from django.urls import path
from . import views

app_name = 'gruposmusculares'

urlpatterns = [
    path('listar/', views.listar_gruposmusculares, name='listar_gruposmusculares'),
    path('adicionar/', views.adicionar_grupomuscular, name='adicionar_grupomuscular'),
    path('editar/<int:id_grupomuscular>/', views.editar_grupomuscular, name='editar_grupomuscular'),
    path('deletar/<int:id_grupomuscular>/', views.deletar_grupomuscular, name='deletar_grupomuscular'),
]