from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('registrar/', views.registrar, name='registrar'),
    path('login/', views.fazer_login, name='login'),
    path('logout/', views.fazer_logout, name='logout'),
    path('carro/', views.carro_list, name='carro_list'),
    path('carro/create/', views.carro_create, name='carro_create'),
    path('carro/<int:pk>/update/', views.carro_update, name='carro_update'),
    path('carro/<int:pk>/delete/', views.carro_delete, name='carro_delete'),
]