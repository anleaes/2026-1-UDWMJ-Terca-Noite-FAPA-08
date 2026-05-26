from django.shortcuts import render, redirect, get_list_or_404
from .forms import CategoriaAlimentoForm
from .models import CategoriaAlimento


def add_categoria_alimento(request):
    template_name = 'categoria-alimento/add_categoria_alimento.html'
    context = {}
    if request.method == 'POST':
        form = CategoriaAlimentoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('core:home')
    form = CategoriaAlimentoForm()
    context['form'] = form
    return render(request, template_name, context)

# Create your views here.
