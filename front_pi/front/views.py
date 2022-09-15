from django.http import HttpResponse
import requests
from django.shortcuts import render


from front_pi.settings import API_URL
from .validators import validaEmail
from .forms import LoginForm


def login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        email = request.POST['login-email']
        password = request.POST['login-password']
        
        if not email:
            mensagem = ['Você preencher o campo de e-mail']
            return render(request, 'auth/auth.html', {'messages': mensagem})
        if not validaEmail(email=email):
            mensagem = ['Você deve digitar um campo de e-mail válido']
            return render(request, 'auth/auth.html', {'messages': mensagem})
        if not password:
            mensagem = ['Você deve digitar uma senha.']
            return render(request, 'auth/auth.html', {'messages': mensagem})

        user = requests.post('http://localhost:9000/auth/login', {'email': email, 'password': password})

        print(user)
        
    else:
        form = LoginForm()
        
    return render(request, 'auth/auth.html', {'form': form})


def home(request):

    return render(request, 'home/home.html', {'titulo': 'Home'})

def clientes(request):

    return render(request, 'clientes/clientes.html', {'titulo': 'Clientes'})

def cadastrar_clientes(request):
    return render(request, 'clientes/cadastrar_clientes.html', {'titulo': 'Cadastro de cliente'})


