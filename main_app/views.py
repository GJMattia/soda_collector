from django.shortcuts import render

sodas = [
    {'name': 'Pepsi', 'color': 'brown',
        'description': 'carbonated cola soft drink', 'release_date': 1965},
    {'name': 'Sprite', 'color': 'clear',
     'description': 'lemon and lime-flavored soft drink', 'release_date': 1961},
]


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def sodas_index(request):
    return render(request, 'sodas/index.html', {
        'sodas': sodas
    })
