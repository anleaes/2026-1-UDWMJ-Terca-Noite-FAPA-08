from django.shortcuts import render, get_object_or_404
from avaliacoesfisicas.models import Avaliacaofisica
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