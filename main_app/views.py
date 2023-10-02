from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Soda, Store
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
    id_list = soda.stores.all().values_list('id')
    stores_soda_doesnt_have = Store.objects.exclude(id__in=id_list)
    consumption_form = ConsumptionForm()
    return render(request, 'sodas/detail.html', {'soda': soda, 'consumption_form': consumption_form, 'stores': stores_soda_doesnt_have})


class SodaCreate(CreateView):
    model = Soda
    fields = ['name', 'parent_company', 'color', 'release_year']


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


class StoreList(ListView):
    model = Store


class StoreDetail(DetailView):
    model = Store


class StoreCreate(CreateView):
    model = Store
    fields = '__all__'


class StoreUpdate(UpdateView):
    model = Store
    fields = ['name', 'state']


class StoreDelete(DeleteView):
    model = Store
    success_url = '/stores'


def assoc_store(request, soda_id, store_id):
    Soda.objects.get(id=soda_id).stores.add(store_id)
    return redirect('detail', soda_id=soda_id)


def de_assoc_store(request, soda_id, store_id):
    Soda.objects.get(id=soda_id).stores.remove(store_id)
    return redirect('detail', soda_id=soda_id)
