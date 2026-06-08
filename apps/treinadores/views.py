from django.shortcuts import render, get_object_or_404, redirect
from .forms import TreinadorForm
from .models import Treinador
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/contas/login/')
def adicionar_treinador(request):
    template_name = 'treinadores/adicionar_treinador.html'
    context = {}
    if request.method == 'POST':
        form = TreinadorForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('treinadores:listar_treinadores')
    form = TreinadorForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def listar_treinadores(request):
    template_name = 'treinadores/listar_treinadores.html'
    treinadores = Treinador.objects.filter()
    context = {
        'treinadores': treinadores,
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def editar_treinador(request, id_treinador):
    template_name = 'treinadores/adicionar_treinador.html'
    context ={}
    treinador = get_object_or_404(Treinador, id=id_treinador)
    if request.method == 'POST':
        form = TreinadorForm(request.POST, instance=treinador)
        if form.is_valid():
            form.save()
            return redirect('treinadores:listar_treinadores')
    form = TreinadorForm(instance=treinador)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def deletar_treinador(request, id_treinador):
    treinador = Treinador.objects.get(id=id_treinador)
    treinador.delete()
    return redirect('treinadores:listar_treinadores')
