from django.shortcuts import render, redirect, get_object_or_404
from .forms import AlunoForm
from .models import Aluno, Fichamedica
from avaliacoesfisicas.views import criar_avaliacaofisica_para_aluno
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/contas/login/')
def adicionar_aluno(request):
    template_name = 'alunos/adicionar_aluno.html'
    context = {}
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            aluno = form.save()
            form.save_m2m()
            criar_avaliacaofisica_para_aluno(aluno)

            return redirect('alunos:listar_alunos')
    form = AlunoForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def listar_alunos(request):
    template_name = 'alunos/listar_alunos.html'
    alunos = Aluno.objects.prefetch_related('fichamedica')
    context = {
        'alunos': alunos,
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def editar_aluno(request, id_aluno):
    template_name = 'alunos/adicionar_aluno.html'
    context ={}
    aluno = get_object_or_404(Aluno, id=id_aluno)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('alunos:listar_alunos')
    form = AlunoForm(instance=aluno)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def deletar_aluno(request, id_aluno):
    aluno = Aluno.objects.get(id=id_aluno)
    aluno.delete()
    return redirect('alunos:listar_alunos')

@login_required(login_url='/contas/login/')
def pesquisar_alunos(request):
    template_name = 'alunos/listar_alunos.html'
    query = request.GET.get('query')
    fichasmedicas = Fichamedica.objects.filter()
    alunos = Aluno.objects.filter(sobrenome__icontains=query)
    context = {
        'alunos': alunos,
        'fichasmedicas': fichasmedicas,
    }
    return render(request,template_name, context)