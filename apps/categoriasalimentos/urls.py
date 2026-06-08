from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'categoriasalimentos'

router = routers.SimpleRouter()
router.register('', views.CategoriaalimentoViewSet,
                basename='categoriasalimentos')

urlpatterns = [
    path('listar/', views.listar_categoriasalimentos,
         name='listar_categoriasalimentos'),

    path('adicionar/', views.adicionar_categoriaalimento,
         name='adicionar_categoriaalimento'),

    path('editar/<int:id_categoriaalimento>/',
         views.editar_categoriaalimento,
         name='editar_categoriaalimento'),

    path('deletar/<int:id_categoriaalimento>/',
         views.deletar_categoriaalimento,
         name='deletar_categoriaalimento'),

    path('api/', include(router.urls)),
]