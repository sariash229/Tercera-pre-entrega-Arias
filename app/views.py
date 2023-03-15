from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout

from .forms import MateriaForm
from .forms import SemestreForm

# Create your views here.

def home(request):
    return render(request, 'home.html')


def materia(request):
    return render(request, 'materias.html')

def capturarDatos(request):
    
    return render(request, 'captura.html')

def calculadora(request, user_id):            ############################################
    user = get_object_or_404(User,pk=user_id)
    materias=Materia.objects.filter(user = user)           #########################################
    return render(request, 'calculadora.html', {'materias':materias})

def calculadora2(request,user_id):
    user = get_object_or_404(User,pk=user_id)
    semestre=Semestre.objects.filter(user = user)
    return render(request, 'calculadoracreditos.html',{'Semestre':semestre})


def prueba(request):
    return render(request, 'prueba.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('/login')
            
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'register.html', context)


def login(request):
    return render(request, 'login.html')

def logoutaccount(request):
    logout(request)
    return redirect('home')

def crearmateria(request, user_id):
    user = get_object_or_404(User,pk=user_id)
    if request.method == 'GET':
        return render(request, 'createmateria.html',{'form':MateriaForm(), 'user':user})
    else:
        try:    
            form = MateriaForm(request.POST)
            newMateria = form.save(commit=False)
            newMateria.user = request.user
            newMateria.user = user
            newMateria.save()
            return redirect('calculadora/', newMateria.user.id)
        except ValueError:
            return render(request,'createmateria.html',{'form':MateriaForm(),'error':'bad data passed in'})

def actualizarmateria(request,user_id, materia_id):
    materia = get_object_or_404(Materia,pk=materia_id,user=request.user)
    if request.method == 'GET':
        form = MateriaForm(instance=materia)
        return render(request, 'actualizarmateria.html',{'materia': materia,'form':form})
    else:
        try:
            form = MateriaForm(request.POST,instance=materia)
            form.save()
            return redirect('../calculadora/', materia.user.id)
        except ValueError:
            return render(request,'actualizarmateria.html',{'materia': materia,'form':form,'error':'Bad data in form'})

def eliminarmateria(request,user_id, materia_id):
    materia = get_object_or_404(Materia, pk=materia_id,user=request.user)
    materia.delete()
    return redirect('../calculadora/', materia.user.id)

def crearsemestre(request, user_id):
    user = get_object_or_404(User,pk=user_id)
    if request.method == 'GET':
        return render(request, 'createsemestre.html',{'form':SemestreForm(), 'user':user})
    else:
        try:    
            form = SemestreForm(request.POST)
            newSemestre = form.save(commit=False)
            newSemestre.user = request.user
            newSemestre.user = user
            newSemestre.save()
            return redirect('calculadoracreditos/', newSemestre.user.id)
        except ValueError:
            return render(request,'createsemestre.html',{'form':SemestreForm(),'error':'bad data passed in'})

