
from django.shortcuts import render, redirect, get_object_or_404
from .forms import GrupoMuscularForm
from .models import CategoriaGrupoMuscular    

def delete_grupomuscular(request, id_grupomuscular):
    grupomuscular = CategoriaGrupoMuscular.objects.get(id=id_grupomuscular)
    grupomuscular.delete()
    return redirect('grupo_muscular:list_grupomuscular')

def edit_grupomuscular(request, id_grupomuscular):
    template_name = 'grupo_muscular/add_grupomuscular.html'
    context ={}
    grupomuscular = get_object_or_404(CategoriaGrupoMuscular, id=id_grupomuscular)
    if request.method == 'POST':
        form = GrupoMuscularForm(request.POST, instance=grupomuscular)
        if form.is_valid():
            form.save()
            return redirect('grupo_muscular:list_grupomuscular')
    form = GrupoMuscularForm(instance=grupomuscular)
    context['form'] = form
    return render(request, template_name, context)

def listar_grupomuscular(request):
    grupos = CategoriaGrupoMuscular.objects.all()

    return render(
        request,
        'grupo_muscular/list_grupomuscular.html',
        {'grupos': grupos}
    )

def add_grupomuscular(request):
    template_name = 'grupo_muscular/add_grupomuscular.html'
    context = {}
    if request.method == 'POST':
        form = GrupoMuscularForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('core:home')
    form = GrupoMuscularForm()
    context['form'] = form
    return render(request, template_name, context)