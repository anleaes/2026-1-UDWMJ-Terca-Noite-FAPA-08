from django.urls import path

from . import views


app_name = 'categoria_alimento'


urlpatterns = [

    path(
        'adicionar/',
        views.add_categoria_alimento,
        name='adicionar'
    ),

]
