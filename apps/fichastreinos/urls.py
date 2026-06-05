from django.urls import path
from . import views

app_name = 'fichastreinos'

urlpatterns = [
    path('exercicios/', views.lista_treinos_exercicios, name='lista_treinos_exercicios'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('carrinho/adicionar/<int:exercicio_id>/', views.adicionar_carrinho, name='adicionar_carrinho'),
    path('carrinho/editar/<int:exercicio_id>/', views.editar_carrinho, name='editar_carrinho'),
    path('carrinho/excluir/<int:exercicio_id>/', views.deletar_carrinho, name='deletar_carrinho'),
    path('checkout/', views.checkout, name='checkout'),
    path('listar/', views.listar_fichastreinos, name='listar_fichastreinos'),
    path('itens/<int:fichatreino_id>/', views.ver_fichatreino, name='ver_fichatreino'),
    path('itens/<int:fichatreino_id>/cancelar/', views.cancelar_fichatreino, name='cancelar_fichatreino'),
]