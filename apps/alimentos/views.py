from django.shortcuts import render, get_object_or_404, redirect
from .forms import AlimentoForm
from .models import Alimento
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/contas/login/')
def adicionar_alimento(request):
    template_name = 'alimentos/adicionar_alimento.html'
    context = {}
    if request.method == 'POST':
        form = AlimentoForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('alimentos:listar_alimentos')
    form = AlimentoForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def listar_alimentos(request):
    template_name = 'alimentos/listar_alimentos.html'
    alimentos = Alimento.objects.filter()
    context = {
        'alimentos': alimentos
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def editar_alimento(request, id_alimento):
    template_name = 'alimentos/adicionar_alimento.html'
    context ={}
    alimento = get_object_or_404(Alimento, id=id_alimento)
    if request.method == 'POST':
        form = AlimentoForm(request.POST, request.FILES,  instance=alimento)
        if form.is_valid():
            form.save()
            return redirect('alimentos:listar_alimentos')
    form = AlimentoForm(instance=alimento)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def deletar_alimento(request, id_alimento):
    alimento = Alimento.objects.get(id=id_alimento)
    alimento.delete()
    return redirect('alimentos:listar_alimentos')