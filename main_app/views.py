from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Soda
from .forms import ConsumptionForm


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
    consumption_form = ConsumptionForm()
    return render(request, 'sodas/detail.html', {'soda': soda, 'consumption_form': consumption_form})


class SodaCreate(CreateView):
    model = Soda
    fields = '__all__'


class SodaUpdate(UpdateView):
    model = Soda
    fields = ['parent_company', 'color', 'release_year']


class SodaDelete(DeleteView):
    model = Soda
    success_url = '/sodas'


def add_consumption(request, soda_id):
    form = ConsumptionForm(request.POST)
    if form.is_valid():
        new_consumption = form.save(commit=False)
        new_consumption.soda_id = soda_id
        new_consumption.save()
    return redirect('detail', soda_id=soda_id)
