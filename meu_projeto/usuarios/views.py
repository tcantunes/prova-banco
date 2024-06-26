from django.shortcuts import render, get_object_or_404, redirect
from .models import Carro
from .forms import CarroForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'base.html')


def registrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registrar.html', {'form': form})


def fazer_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('carro_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def fazer_logout(request):
    logout(request)
    return redirect('login')


def carro_list(request):
    carros = Carro.objects.all()
    return render(request, 'carro_list.html', {'carros': carros})


def carro_create(request):
    if request.method == 'POST':
        form = CarroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('carro_list')
    else:
        form = CarroForm()
    return render(request, 'carro_form.html', {'form': form})


def carro_update(request, pk):
    carro = get_object_or_404(Carro, pk=pk)
    if request.method == 'POST':
        form = CarroForm(request.POST, instance=carro)
        if form.is_valid():
            form.save()
            return redirect('carro_list')
    else:
        form = CarroForm(instance=carro)
    return render(request, 'carro_form.html', {'form': form})




def carro_delete(request, pk):
    carro = get_object_or_404(Carro, pk=pk)
    if request.method == 'POST':
        carro.delete()
        return redirect('carro_list')
    return render(request, 'carro_confirm_delete.html', {'carro': carro})


