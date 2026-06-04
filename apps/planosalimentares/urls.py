from django.urls import path
from . import views

app_name = 'planosalimentares'

urlpatterns = [
    path('alimentos/', views.lista_refeicoes_alimentos, name='lista_refeicoes_alimentos'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('carrinho/adicionar/<int:alimento_id>/', views.adicionar_carrinho, name='adicionar_carrinho'),
    path('carrinho/editar/<int:alimento_id>/', views.editar_carrinho, name='editar_carrinho'),
    path('carrinho/excluir/<int:alimento_id>/', views.deletar_carrinho, name='deletar_carrinho'),
    path('checkout/', views.checkout, name='checkout'),
    path('listar/', views.listar_planosalimentares, name='listar_planosalimentares'),
    path('itens/<int:planoalimentar_id>/', views.ver_planoalimentar, name='ver_planoalimentar'),
    path('itens/<int:planoalimentar_id>/cancelar/', views.cancelar_planoalimentar, name='cancelar_planoalimentar'),
]