from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('sodas/', views.sodas_index, name='index'),
    path('soda/<int:soda_id>/', views.sodas_detail, name='detail'),
    path('sodas/create/', views.SodaCreate.as_view(), name='sodas_create'),
    path('sodas/<int:pk>/update/', views.SodaUpdate.as_view(), name='sodas_update'),
    path('sodas/<int:pk>/delete/', views.SodaDelete.as_view(), name='sodas_delete'),

]
