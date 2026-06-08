from django.shortcuts import render, get_object_or_404, redirect
from planosalimentares.models import Planoalimentar
from refeicoes.models import Refeicao
from alimentos.models import Alimento
from nutricionistas.models import Nutricionista
from alunos.models import Aluno
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/contas/login/')
def listar_planosalimentares(request):
    template_name = 'planosalimentares/listar_planosalimentares.html'
    planosalimentares = Planoalimentar.objects.select_related('aluno', 'nutricionista').all()
    context = {
        'planosalimentares': planosalimentares,
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def lista_refeicoes_alimentos(request):
    template_name = 'planosalimentares/lista_refeicoes_alimentos.html'
    alimentos = Alimento.objects.filter(esta_ativo=True)
    context = {
        'alimentos': alimentos,
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def carrinho(request):
    template_name = 'planosalimentares/carrinho.html'
    carrinho = request.session.get('carrinho', {})
    total = 0.0
    for chave, item in carrinho.items():
        total += int(item.get('quantidade', 0))
    context = {
        'carrinho': carrinho,
        'total': total,
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def adicionar_carrinho(request, alimento_id):
    alimento = get_object_or_404(Alimento, id=alimento_id)
    carrinho = request.session.get('carrinho', {})
    pid = str(alimento.id)
    if pid in carrinho:
        carrinho[pid]['quantidade'] += 100
    else:
        carrinho[pid] = {
            'nome': alimento.nome,
            'quantidade': 100,
            'observacao': '',
            'refeicao': ''
        }
    quantidade = carrinho[pid]['quantidade']
    request.session['carrinho'] = carrinho
    request.session.modified = True
    return redirect('planosalimentares:carrinho')

@login_required(login_url='/contas/login/')
def editar_carrinho(request, alimento_id):
    if request.method == 'POST':
        quantidade = int(request.POST.get('quantidade', 1))
        observacao = str(request.POST.get('observacao', ''))
        refeicao = str(request.POST.get('refeicao', ''))
        carrinho = request.session.get('carrinho', {})
        pid = str(alimento_id)
        if pid in carrinho:
            if quantidade <= 0:
                del carrinho[pid]
            else:
                carrinho[pid]['quantidade'] = quantidade
                carrinho[pid]['observacao'] = observacao
                carrinho[pid]['refeicao'] = refeicao
        request.session['carrinho'] = carrinho
        request.session.modified = True
    return redirect('planosalimentares:carrinho')

@login_required(login_url='/contas/login/')
def deletar_carrinho(request, alimento_id):
    carrinho = request.session.get('carrinho', {})
    pid = str(alimento_id)
    if pid in carrinho:
        del carrinho[pid]
    request.session['carrinho'] = carrinho
    request.session.modified = True
    return redirect('planosalimentares:carrinho')

@login_required(login_url='/contas/login/')
def checkout(request):
    template_name = 'planosalimentares/checkout.html'
    carrinho = request.session.get('carrinho', {})
    if request.method == 'POST':
        aluno_id = request.POST.get('aluno')
        nutricionista_id = request.POST.get('nutricionista')
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        esta_ativo = request.POST.get('esta_ativo')
        aluno = get_object_or_404(Aluno, id=aluno_id)
        nutricionista = get_object_or_404(Nutricionista, id=nutricionista_id)
        planoalimentar = Planoalimentar.objects.create(
            aluno=aluno,
            nutricionista=nutricionista,
            nome=nome,
            descricao=descricao,
            esta_ativo=esta_ativo
        )
        for alimento_id, item in carrinho.items():
            alimento = get_object_or_404(Alimento, id=alimento_id)
            quantidade = int(item['quantidade'])
            observacao = str(item['observacao'])
            refeicao = str(item.get('refeicao', ''))
            Refeicao.objects.create(
                plano_alimentar=planoalimentar,
                alimento=alimento,
                quantidade_gramas=quantidade,
                observacao=observacao,
                dia_refeicao=refeicao
            )
        request.session['carrinho'] = {}
        request.session.modified = True
        return redirect('planosalimentares:listar_planosalimentares')

    alunos = Aluno.objects.all()
    nutricionistas = Nutricionista.objects.all()

    context = {
        'carrinho': carrinho,
        'alunos': alunos,
        'nutricionistas': nutricionistas,
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def cancelar_planoalimentar(request, planoalimentar_id):
    planoalimentar = get_object_or_404(Planoalimentar, id=planoalimentar_id)
    if planoalimentar.esta_ativo != False:
        planoalimentar.esta_ativo = False
        planoalimentar.save()
    return redirect('planosalimentares:listar_planosalimentares')

@login_required(login_url='/contas/login/')
def ver_planoalimentar(request, planoalimentar_id):
    template_name = 'planosalimentares/ver_planoalimentar.html'
    planoalimentar = get_object_or_404(Planoalimentar, id=planoalimentar_id)
    items = planoalimentar.planosalimentares.all()
    context = {
        'planoalimentar': planoalimentar,
        'items': items,
    }
    return render(request, template_name, context)