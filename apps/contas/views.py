from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UsuarioForm, UsuarioAlterarInformacoesForm

def adicionar_usuario(request):
    template_name = 'contas/adicionar_usuario.html'
    context = {}
    if request.method =='POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.set_password(f.password)
            f.save()
            return redirect('contas:usuario_login')
        else:
            return redirect('contas:adicionar_usuario')
    form = UsuarioForm()
    context['form'] = form
    return render(request, template_name, context)

def usuario_login(request):
    template_name = 'contas/usuario_login.html'
    if request.method =='POST':
        nome_usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        usuario = authenticate(username=nome_usuario, password=senha)
        if usuario is not None:
            login(request, usuario)
            return redirect(request.GET.get('next', '/'))
        else:
            return redirect('contas:usuario_login')
    return render(request, template_name, {})

@login_required(login_url='/contas/login/')
def usuario_logout(request):
    logout(request)
    return redirect('contas:usuario_login')

@login_required(login_url='/contas/login/')
def usuario_alterar_senha(request):
    template_name = 'contas/usuario_alterar_senha.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
        else:
            return redirect('contas:usuario_login')
    form = PasswordChangeForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def usuario_alterar_informacoes(request, username):
    template_name = 'contas/usuario_alterar_informacoes.html'
    context = {}
    usuario = User.objects.get(username=username)
    if request.method == 'POST':
        form = UsuarioAlterarInformacoesForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UsuarioAlterarInformacoesForm(instance=usuario)
    
    context['form'] = form
    return render(request, template_name, context)