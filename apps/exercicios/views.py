from django.shortcuts import render, get_object_or_404, redirect
from .forms import ExercicioForm
from .models import Exercicio
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/contas/login/')
def adicionar_exercicio(request):
    template_name = 'exercicios/adicionar_exercicio.html'
    context = {}
    if request.method == 'POST':
        form = ExercicioForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('exercicios:listar_exercicios')
    form = ExercicioForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def listar_exercicios(request):
    template_name = 'exercicios/listar_exercicios.html'
    exercicios = Exercicio.objects.filter()
    context = {
        'exercicios': exercicios
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def editar_exercicio(request, id_exercicio):
    template_name = 'exercicios/adicionar_exercicio.html'
    context ={}
    exercicio = get_object_or_404(Exercicio, id=id_exercicio)
    if request.method == 'POST':
        form = ExercicioForm(request.POST, request.FILES,  instance=exercicio)
        if form.is_valid():
            form.save()
            return redirect('exercicios:listar_exercicios')
    form = ExercicioForm(instance=exercicio)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def deletar_exercicio(request, id_exercicio):
    exercicio = Exercicio.objects.get(id=id_exercicio)
    exercicio.delete()
    return redirect('exercicios:listar_exercicios')