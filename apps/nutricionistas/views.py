from django.shortcuts import render, get_object_or_404, redirect
from .forms import NutricionistaForm
from .models import Nutricionista
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/contas/login/')
def adicionar_nutricionista(request):
    template_name = 'nutricionistas/adicionar_nutricionista.html'
    context = {}
    if request.method == 'POST':
        form = NutricionistaForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('nutricionistas:listar_nutricionistas')
    form = NutricionistaForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def listar_nutricionistas(request):
    template_name = 'nutricionistas/listar_nutricionistas.html'
    nutricionistas = Nutricionista.objects.filter()
    context = {
        'nutricionistas': nutricionistas,
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def editar_nutricionista(request, id_nutricionista):
    template_name = 'nutricionistas/adicionar_nutricionista.html'
    context ={}
    nutricionista = get_object_or_404(Nutricionista, id=id_nutricionista)
    if request.method == 'POST':
        form = NutricionistaForm(request.POST, instance=nutricionista)
        if form.is_valid():
            form.save()
            return redirect('nutricionistas:listar_nutricionistas')
    form = NutricionistaForm(instance=nutricionista)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def deletar_nutricionista(request, id_nutricionista):
    nutricionista = Nutricionista.objects.get(id=id_nutricionista)
    nutricionista.delete()
    return redirect('nutricionistas:listar_nutricionistas')
