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
    path('sodas/<int:soda_id>/add_feeding/',
         views.add_consumption, name='add_consumption'),

    path('sodas/<int:soda_id>/assoc_store/<int:store_id>/',
         views.assoc_store, name='assoc_store'),

    path('sodas/<int:soda_id>/de_assoc_store/<int:store_id>/',
         views.de_assoc_store, name='de_assoc_store'),

    path('stores/', views.StoreList.as_view(), name='stores_index'),

    path('stores/<int:pk>/', views.StoreDetail.as_view(), name='stores_detail'),

    path('stores/create/', views.StoreCreate.as_view(), name='stores_create'),

    path('stores/<int:pk>/update/',
         views.StoreUpdate.as_view(), name='stores_update'),

    path('stores/<int:pk>/delete/',
         views.StoreDelete.as_view(), name='stores_delete'),
]
