from django.shortcuts import render

from .models import Soda


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def sodas_index(request):
    sodas = Soda.objects.all()
    return render(request, 'sodas/index.html', {
        'sodas': sodas
    })


def sodas_detail(request, soda_id):
    soda = Soda.objects.get(id=soda_id)
    return render(request, 'sodas/detail.html', {'soda': soda})
