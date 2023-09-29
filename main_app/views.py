from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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


class SodaCreate(CreateView):
    model = Soda
    fields = '__all__'


class SodaUpdate(UpdateView):
    model = Soda
    fields = ['parent_company', 'color', 'release_year']


class SodaDelete(DeleteView):
    model = Soda
    success_url = '/sodas'
