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
    if request.method == 'POST':
        form = PlanetaForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('planetario:list_planetas')
    
    form = PlanetaForm()
    return render(request, 'planeta-form.html', {'form': form})

def update_planeta(request, id):
    planeta = Planeta.objects.get(id=id)
    form = PlanetaForm(instance = planeta )
    if request.method == 'POST':
        form = PlanetaForm(data = request.POST,files= request.FILES, instance = planeta )

        if form.is_valid():
            form.save()
            return redirect('planetario:list_planetas')

        return render(request, 'planeta-form.html', {'form': form, 'planeta': planeta})
    else:
        return render(request, 'planeta-form.html', {'form': form, 'planeta': planeta})


def delete_planeta(request, id):
    planeta = Planeta.objects.get(id=id)

    if request.method == 'POST':
        planeta.delete()
        return redirect('planetario:list_planetas')

    return render(request, 'delete-confirm.html', {'planeta': planeta})