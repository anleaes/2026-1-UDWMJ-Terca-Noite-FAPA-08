from django.urls import path
from . import views

app_name = 'contas'

urlpatterns = [
    path('novo-usuario/',views.adicionar_usuario, name='adicionar_usuario'),
    path('login/',views.usuario_login, name='usuario_login'),
    path('sair/',views.usuario_logout, name='usuario_logout'),
    path('alterar-senha/',views.usuario_alterar_senha, name='usuario_alterar_senha'),
    path('alterar-usuario/<username>/',views.usuario_alterar_informacoes, name='usuario_alterar_informacoes'),
]
