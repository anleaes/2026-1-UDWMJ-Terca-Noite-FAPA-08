from django.shortcuts import render, get_object_or_404, redirect
from avaliacoesfisicas.models import Avaliacaofisica
from avaliacoesfisicas.forms import AvaliacaofisicaForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/contas/login/')
def criar_avaliacaofisica_para_aluno(aluno):
    if hasattr(aluno, 'avaliacaofisica'):
        return aluno.avaliacaofisica

    numero_avaliacao = f'A-{aluno.id:06d}' 

    return Avaliacaofisica.objects.create(
        aluno=aluno,
        numero=numero_avaliacao
    )

@login_required(login_url='/contas/login/')
def ver_avaliacaofisica(request, avaliacaofisica_id):
    template_name = 'avaliacoesfisicas/ver_avaliacaofisica.html'
    avaliacaofisica = get_object_or_404(Avaliacaofisica, id=avaliacaofisica_id)

    context = {
        'avaliacaofisica': avaliacaofisica,
        'aluno': avaliacaofisica.aluno,
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def listar_avaliacoesfisicas(request):
    template_name = 'avaliacoesfisicas/listar_avaliacoesfisicas.html'
    avaliacoesfisicas = Avaliacaofisica.objects.all()
    context = {
        'avaliacoesfisicas': avaliacoesfisicas,
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def adicionar_avaliacaofisica(request):
    template_name = 'avaliacoesfisicas/adicionar_avaliacaofisica.html'
    context = {}
    if request.method == 'POST':
        form = AvaliacaofisicaForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.numero = f'A-{f.aluno.id:06d}'
            f.imc = f.calcular_imc
            f.save()
            return redirect('avaliacoesfisicas:listar_avaliacoesfisicas')
    else:
        form = AvaliacaofisicaForm()
    
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def editar_avaliacaofisica(request, avaliacaofisica_id):
    template_name = 'avaliacoesfisicas/adicionar_avaliacaofisica.html'
    context = {}
    avaliacaofisica = get_object_or_404(Avaliacaofisica, id=avaliacaofisica_id)
    if request.method == 'POST':
        form = AvaliacaofisicaForm(request.POST, instance=avaliacaofisica)
        if form.is_valid():
            f = form.save(commit=False)
            f.imc = f.calcular_imc
            f.save()
            return redirect('avaliacoesfisicas:listar_avaliacoesfisicas')
    else:
        form = AvaliacaofisicaForm(instance=avaliacaofisica)
    
    context['form'] = form
    context['avaliacaofisica'] = avaliacaofisica
    return render(request, template_name, context)