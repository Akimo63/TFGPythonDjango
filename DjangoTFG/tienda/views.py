from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Categoria
from .forms import CatForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def tienda(request):
    categorias = Categoria.objects.all()  # Obtener todas las categorías
    return render(request, 'tienda.html', {
        'categorias': categorias
        })
    # return render(request, 'tienda.html')

def categoria(request, categoria_id):
    if request.method == 'GET':
        categoria = get_object_or_404(Categoria, pk=categoria_id)
        return render(request, 'categoria.html', {
            'categorias': categoria

        })
    else:
        categoria = get_object_or_404(Categoria, pk=categoria_id)
        return redirect('tienda')
   
def producto(request, producto_id):
    if request.method == 'GET':
        producto = get_object_or_404(Categoria, pk=producto_id)
        return render(request, 'producto.html', {
            'producto': producto

        })
    else:
        categproductoria = get_object_or_404(Categoria, pk=producto_id)
        return redirect('categoria')
  

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        # Verificar si el email ya está registrado
        if User.objects.filter(email=email).exists():
            messages.error(request, "Este correo ya está registrado. Intenta con otro.")
            return redirect("register")

        # Si el email no existe, crea el usuario
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Cuenta creada con éxito. Ahora puedes iniciar sesión.")
        return redirect("login")

    return render(request, "register.html")

@login_required
def signout(request):
    logout(request)
    return redirect('home')

def signin (request):
    
    if request.method == 'GET':
        return render(request, 'login.html', {
        'form' : AuthenticationForm
    })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
        if user is None:
            return render(request, 'login.html', {
                'form' : AuthenticationForm,
                'error' : 'Username or password wrong'
                })
        else:
            login(request, user)
            return redirect('tasks')