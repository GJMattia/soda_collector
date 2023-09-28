from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('sodas/', views.sodas_index, name='index'),
    path('soda/<int:soda_id>/', views.sodas_detail, name='detail'),

]
