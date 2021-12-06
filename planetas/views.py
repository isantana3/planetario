from django.shortcuts import render, redirect
from .models import Planeta
from .forms import PlanetaForm


def list_planetas(request):
    planetas = Planeta.objects.all()
    if len(planetas) > 0:
        return render(request, 'planetas.html', {'planetas': planetas})
    else:
        return redirect('planetario:create_planeta')

def detail_planeta(request, id):
    planeta = Planeta.objects.get(id=id)
    return render(request, 'planeta-detail.html', {'planeta': planeta})


def create_planeta(request):
    form = PlanetaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('planetario:list_planetas')

    return render(request, 'planeta-form.html', {'form': form})


def update_planeta(request, id):
    planeta = Planeta.objects.get(id=id)
    form = PlanetaForm(request.POST or None, instance=planeta)

    if form.is_valid():
        form.save()
        return redirect('planetario:list_planetas')

    return render(request, 'planeta-form.html', {'form': form, 'planeta': planeta})


def delete_planeta(request, id):
    planeta = Planeta.objects.get(id=id)

    if request.method == 'POST':
        planeta.delete()
        return redirect('planetario:list_planetas')

    return render(request, 'delete-confirm.html', {'planeta': planeta})