from django.shortcuts import render, get_object_or_404, redirect
from .forms import GrupomuscularForm
from .models import Grupomuscular
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/contas/login/')
def adicionar_grupomuscular(request):
    template_name = 'gruposmusculares/adicionar_grupomuscular.html'
    context = {}
    if request.method == 'POST':
        form = GrupomuscularForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('core:home')
    form = GrupomuscularForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def listar_gruposmusculares(request):
    template_name = 'gruposmusculares/listar_gruposmusculares.html'
    gruposmusculares = Grupomuscular.objects.filter()
    context = {
        'gruposmusculares': gruposmusculares
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def editar_grupomuscular(request, id_grupomuscular):
    template_name = 'gruposmusculares/adicionar_grupomuscular.html'
    context ={}
    grupomuscular = get_object_or_404(Grupomuscular, id=id_grupomuscular)
    if request.method == 'POST':
        form = GrupomuscularForm(request.POST, instance=grupomuscular)
        if form.is_valid():
            form.save()
            return redirect('gruposmusculares:listar_gruposmusculares')
    form = GrupomuscularForm(instance=grupomuscular)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def deletar_grupomuscular(request, id_grupomuscular):
    grupomuscular = Grupomuscular.objects.get(id=id_grupomuscular)
    grupomuscular.delete()
    return redirect('gruposmusculares:listar_gruposmusculares')
