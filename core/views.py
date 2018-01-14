from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tarefas.models import Tarefa
from tarefas.views import lista_tarefas
# Create your views here.

@login_required
def home(request):
    # tarefas = Tarefa.objects.filter(user=request.user, status='')
    #
    # context = {
    #     'tarefas': tarefas
    # }

    return lista_tarefas(request)