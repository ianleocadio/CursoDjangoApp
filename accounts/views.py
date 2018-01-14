from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
import sys
from .forms import CreateUserForm, LoginUserForm
# Create your views here.

def add_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            u = form.save()
            u.set_password(u.password)
            u.save()
            return HttpResponse('Usuário criado com sucesso!')
    else:
        form = CreateUserForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/add_user.html', context)

def login_user(request):
    if request.method == 'POST':
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        form = LoginUserForm(request.POST)
        user = authenticate(username=form.data['username'], password=form.data['password'])
        if user:
            login(request, user)
            return redirect(request.GET.get('next', '/'))
        else:
            messages.error(request, 'Usuário ou senha inválido.')

    context = {
        'form': LoginUserForm()
    }
    return render(request, 'accounts/login_user.html', context)

def logout_user(request):
    logout(request)
    return redirect('accounts:login_user')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Senha alterada com sucesso!')
            return redirect('accounts:change_password')
        else:
            messages.error(request, "Não foi possível alterar sua senha")
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'accounts/change_password.html', {'form': form})
