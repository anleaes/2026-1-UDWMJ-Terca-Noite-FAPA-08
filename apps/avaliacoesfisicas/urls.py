from django.urls import path
from . import views

app_name = 'avaliacoesfisicas'

urlpatterns = [
    path('', views.listar_avaliacoesfisicas, name='listar_avaliacoesfisicas'),
    path('adicionar/', views.adicionar_avaliacaofisica, name='adicionar_avaliacaofisica'),
    path('<int:avaliacaofisica_id>/', views.ver_avaliacaofisica, name='ver_avaliacaofisica'),
    path('editar/<int:avaliacaofisica_id>/', views.editar_avaliacaofisica, name='editar_avaliacaofisica'),
]