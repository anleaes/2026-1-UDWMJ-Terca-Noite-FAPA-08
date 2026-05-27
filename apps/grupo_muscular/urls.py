from django.urls import path
from . import views

app_name = 'grupo_muscular'

urlpatterns = [
    path('adicionar/', views.add_grupomuscular, name='add_grupomuscular'),
    path('listar/', views.listar_grupomuscular, name='list_grupomuscular'),
    path('editar/<int:id_grupomuscular>/', views.edit_grupomuscular, name='edit_grupomuscular'),
    path('excluir/<int:id_grupomuscular>/', views.delete_grupomuscular, name='delete_grupomuscular'),
]