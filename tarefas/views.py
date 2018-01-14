from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Categoria, Tarefa
from .forms import CategoriaForm, TarefaForm

from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def nova_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect('tarefas:lista_categorias')
        else:
            print(form.errors)
    else:
        form = CategoriaForm()
    return render(request, 'tarefas/nova_categoria.html', {'form': form})

@login_required
def lista_categorias(request):
    c = Categoria.objects.filter(user=request.user)

    context = {
        'categorias': c
    }

    return render(request, 'tarefas/lista_categorias.html', context)

@login_required
def edita_categoria(request, id):
    c = get_object_or_404(Categoria, id=id, user=request.user)

    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=c)
        if form.is_valid():
            form.save()
            return redirect('tarefas:lista_categorias')
    else:
        form = CategoriaForm(instance=c)

    context = {
        'form': form
    }

    return render(request, 'tarefas/nova_categoria.html', context)

@login_required
def delete_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    if categoria.user == request.user:
        categoria.delete()
    else:
        messages.error(request, 'Este usuário não possuí permissão para exclusão desta categoria')
        return render(request, 'tarefas/lista_categorias.html')
    return redirect('tarefas:lista_categorias')

@login_required
def nova_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(user=request.user, data=request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect('tarefas:lista_tarefas')
        else:
            print(form.errors)
    else:
        form = TarefaForm(user=request.user)
    return render(request, 'tarefas/nova_tarefa.html', {'form_tarefa': form})

@login_required
def lista_tarefas(request):
    t = Tarefa.objects.filter(user=request.user, status='')

    context = {
        'tarefas': t
    }

    return render(request, 'core/index.html', context)

@login_required
def edita_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id, user=request.user)

    if request.method == 'POST':
        form = TarefaForm(user=request.user, data=request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('core')
    else:
        form = TarefaForm(user=request.user, editing=True, instance=tarefa)

    context = {
        'form_tarefa': form
    }
    return render(request, 'tarefas/nova_tarefa.html', context)

@login_required
def delete_tarefa(request, id):
    tarefa = Tarefa.objects.get(id=id)
    if tarefa.user == request.user:
        tarefa.delete()
    else:
        messages.error(request, 'Este usuário não possuí permissão para exclusão desta tarefa')
        return render(request, 'core/index.html')
    return redirect('core')

@login_required
def detalhes_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id, user=request.user)
    form = TarefaForm(user=request.user, instance=tarefa)
    return render(request, 'tarefas/detalhes_tarefa.html', {'form': form})

#Searchs
@login_required
def search(request):
    q = request.GET.get('search')
    if q is not None:
        result = Tarefa.objects.search(q, request.user)
    return render(request, 'tarefas/pagina_resultado.html', {'result': result})


