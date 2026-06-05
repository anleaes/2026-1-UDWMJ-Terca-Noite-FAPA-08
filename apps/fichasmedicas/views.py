from django.shortcuts import render, get_object_or_404, redirect
from .forms import FichamedicaForm
from .models import Fichamedica

# Create your views here.
def adicionar_fichamedica(request):
    template_name = 'fichasmedicas/adicionar_fichamedica.html'
    context = {}
    if request.method == 'POST':
        form = FichamedicaForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('fichasmedicas:listar_fichasmedicas')
    form = FichamedicaForm()
    context['form'] = form
    return render(request, template_name, context)

def listar_fichasmedicas(request):
    template_name = 'fichasmedicas/listar_fichasmedicas.html'
    fichasmedicas = Fichamedica.objects.filter()
    context = {
        'fichasmedicas': fichasmedicas
    }
    return render(request, template_name, context)

def editar_fichamedica(request, id_fichamedica):
    template_name = 'fichasmedicas/adicionar_fichamedica.html'
    context ={}
    fichamedica = get_object_or_404(Fichamedica, id=id_fichamedica)
    if request.method == 'POST':
        form = FichamedicaForm(request.POST, instance=fichamedica)
        if form.is_valid():
            form.save()
            return redirect('fichasmedicas:listar_fichasmedicas')
    form = FichamedicaForm(instance=fichamedica)
    context['form'] = form
    return render(request, template_name, context)

def deletar_fichamedica(request, id_fichamedica):
    fichamedica = Fichamedica.objects.get(id=id_fichamedica)
    fichamedica.delete()
    return redirect('fichasmedicas:listar_fichasmedicas')