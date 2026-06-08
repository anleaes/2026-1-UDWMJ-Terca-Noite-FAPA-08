from django.shortcuts import render, get_object_or_404, redirect
from fichastreinos.models import Fichatreino
from diastreinos.models import Diatreino
from exercicios.models import Exercicio
from alunos.models import Aluno
from treinadores.models import Treinador
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/contas/login/')
def listar_fichastreinos(request):
    template_name = 'fichastreinos/listar_fichastreinos.html'
    fichastreinos = Fichatreino.objects.select_related('aluno', 'treinador').all()
    context = {
        'fichastreinos': fichastreinos,
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def lista_treinos_exercicios(request):
    template_name = 'fichastreinos/lista_treinos_exercicios.html'
    exercicios = Exercicio.objects.filter(esta_ativo=True)
    context = {
        'exercicios': exercicios,
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def carrinho(request):
    template_name = 'fichastreinos/carrinho.html'
    carrinho = request.session.get('carrinho', {})
    total = 0.0
    for chave, item in carrinho.items():
        total += int(item.get('serie', 0))
    context = {
        'carrinho': carrinho,
        'total': total,
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def adicionar_carrinho(request, exercicio_id):
    exercicio = get_object_or_404(Exercicio, id=exercicio_id)
    carrinho = request.session.get('carrinho', {})
    pid = str(exercicio.id)
    if pid in carrinho:
        carrinho[pid]['serie'] += 1
    else:
        carrinho[pid] = {
            'nome': exercicio.nome,
            'serie': 1,
            'repeticao': 12,
            'intervalo': 30,
            'observacao': '',
            'dia_treino': ''
        }
    serie = carrinho[pid]['serie']
    request.session['carrinho'] = carrinho
    request.session.modified = True
    return redirect('fichastreinos:carrinho')

@login_required(login_url='/contas/login/')
def editar_carrinho(request, exercicio_id):
    if request.method == 'POST':
        serie = int(request.POST.get('serie', 1))
        repeticao = int(request.POST.get('repeticao', 1))
        intervalo = int(request.POST.get('intervalo', 1))
        observacao = str(request.POST.get('observacao', ''))
        dia_treino = request.POST.get('dia_treino', '')
        carrinho = request.session.get('carrinho', {})
        pid = str(exercicio_id)
        if pid in carrinho:
            if serie <= 0:
                del carrinho[pid]
            else:
                carrinho[pid]['serie'] = serie
                carrinho[pid]['repeticao'] = repeticao
                carrinho[pid]['intervalo'] = intervalo
                carrinho[pid]['observacao'] = observacao
                carrinho[pid]['dia_treino'] = dia_treino
        request.session['carrinho'] = carrinho
        request.session.modified = True
    return redirect('fichastreinos:carrinho')

@login_required(login_url='/contas/login/')
def deletar_carrinho(request, exercicio_id):
    carrinho = request.session.get('carrinho', {})
    pid = str(exercicio_id)
    if pid in carrinho:
        del carrinho[pid]
    request.session['carrinho'] = carrinho
    request.session.modified = True
    return redirect('fichastreinos:carrinho')

@login_required(login_url='/contas/login/')
def checkout(request):
    template_name = 'fichastreinos/checkout.html'
    carrinho = request.session.get('carrinho', {})
    if request.method == 'POST':
        aluno_id = request.POST.get('aluno')
        treinador_id = request.POST.get('treinador')
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        esta_ativo = request.POST.get('esta_ativo')
        aluno = get_object_or_404(Aluno, id=aluno_id)
        treinador = get_object_or_404(Treinador, id=treinador_id)
        fichatreino = Fichatreino.objects.create(
            aluno=aluno,
            treinador=treinador,
            nome=nome,
            descricao=descricao,
            esta_ativo=esta_ativo
        )
        for exercicio_id, item in carrinho.items():
            exercicio = get_object_or_404(Exercicio, id=exercicio_id)
            serie = int(item['serie'])
            repeticao = int(item['repeticao'])
            intervalo = int(item['intervalo'])
            observacao = str(item['observacao'])
            dia_treino = str(item.get('dia_treino', ''))
            Diatreino.objects.create(
                ficha_treino=fichatreino,
                exercicio=exercicio,
                serie=serie,
                repeticao=repeticao,
                intervalo=intervalo,
                observacao=observacao,
                nome=dia_treino
            )
        request.session['carrinho'] = {}
        request.session.modified = True
        return redirect('fichastreinos:listar_fichastreinos')

    alunos = Aluno.objects.all()
    treinadores = Treinador.objects.all()

    context = {
        'carrinho': carrinho,
        'alunos': alunos,
        'treinadores': treinadores,
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def cancelar_fichatreino(request, fichatreino_id):
    fichatreino = get_object_or_404(Fichatreino, id=fichatreino_id)
    if fichatreino.esta_ativo != False:
        fichatreino.esta_ativo = False
        fichatreino.save()
    return redirect('fichastreinos:listar_fichastreinos')

@login_required(login_url='/contas/login/')
def ver_fichatreino(request, fichatreino_id):
    template_name = 'fichastreinos/ver_fichatreino.html'
    fichatreino = get_object_or_404(Fichatreino, id=fichatreino_id)
    items = fichatreino.fichastreinos.all()
    context = {
        'fichatreino': fichatreino,
        'items': items,
    }
    return render(request, template_name, context)