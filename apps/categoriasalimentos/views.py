from django.shortcuts import render, get_object_or_404, redirect
from .forms import CategoriaalimentoForm
from .models import Categoriaalimento

# Create your views here.
def adicionar_categoriaalimento(request):
    template_name = 'categoriasalimentos/adicionar_categoriaalimento.html'
    context = {}
    if request.method == 'POST':
        form = CategoriaalimentoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('core:home')
    form = CategoriaalimentoForm()
    context['form'] = form
    return render(request, template_name, context)

def listar_categoriasalimentos(request):
    template_name = 'categoriasalimentos/listar_categoriasalimentos.html'
    categoriasalimentos = Categoriaalimento.objects.filter()
    context = {
        'categoriasalimentos': categoriasalimentos
    }
    return render(request, template_name, context)

def editar_categoriaalimento(request, id_categoriaalimento):
    template_name = 'categoriasalimentos/adicionar_categoriaalimento.html'
    context ={}
    categoriaalimento = get_object_or_404(Categoriaalimento, id=id_categoriaalimento)
    if request.method == 'POST':
        form = CategoriaalimentoForm(request.POST, instance=categoriaalimento)
        if form.is_valid():
            form.save()
            return redirect('categoriasalimentos:listar_categoriasalimentos')
    form = CategoriaalimentoForm(instance=categoriaalimento)
    context['form'] = form
    return render(request, template_name, context)

def deletar_categoriaalimento(request, id_categoriaalimento):
    categoriaalimento = Categoriaalimento.objects.get(id=id_categoriaalimento)
    categoriaalimento.delete()
    return redirect('categoriasalimentos:listar_categoriasalimentos')
