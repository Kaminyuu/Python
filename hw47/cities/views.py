from django.shortcuts import render, get_object_or_404, redirect
from .models import Cities, Sights
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


def cities(request):
    attractions = Cities.objects.all()
    return render(request, 'cities/cities.html', {'attractions': attractions})


def sights(request):
    sight = Sights.objects.all()
    return render(request, 'cities/sights.html', {'sight': sight})


def description(request, sights_id):
    objects = get_object_or_404(Sights, pk=sights_id)
    return render(request, 'cities/description.html', {'objects': objects})


def signup(request):
    if request.method == "GET":
        return render(request, 'cities/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('cities')
            except IntegrityError:
                return render(request, 'cities/signupuser.html', {'form': UserCreationForm(),
                                                                  'error': 'Такой логин уже существует, задайте другой.'})
        else:
            return render(request, 'cities/signupuser.html', {'form': UserCreationForm(),
                                                              'error': 'Пароли не совпадают'})


def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('cities')


def loginuser(request):
    if request.method == "GET":
        return render(request, 'cities/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'cities/loginuser.html', {'form': AuthenticationForm(),
                                                           'error': "Неверные данные для входа"})
        else:
            login(request, user)
            return redirect('cities')
