from django.urls import path
from . import views

app_name = "tarefas"
urlpatterns = [
    path('nova-categoria/', views.nova_categoria, name='nova_categoria'),
    path('lista-categorias/', views.lista_categorias, name='lista_categorias'),
    path('edita-categoria/<id>', views.edita_categoria, name='edita_categoria'),
    path('delete-categoria/<id>', views.delete_categoria, name='delete_categoria'),

    path('nova-tarefa/', views.nova_tarefa, name='nova_tarefa'),
    path('lista-tarefas/', views.lista_tarefas, name='lista_tarefas'),
    path('edita-tarefa/<id>', views.edita_tarefa, name='edita_tarefa'),
    path('delete-tarefa/<id>', views.delete_tarefa, name='delete_tarefa'),
    path('detalhes-tarefa/<id>', views.detalhes_tarefa, name='detalhes_tarefa'),

    path('busca/', views.search, name='search'),
]