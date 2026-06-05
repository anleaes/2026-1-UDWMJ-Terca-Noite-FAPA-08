app_name = 'avaliacoesfisicas'

urlpatterns = [
    path('<int:avaliacaofisica_id>/', views.ver_avaliacaofisica, name='ver_avaliacoesfisica'),
]