import requests
from django.shortcuts import render
from .validators import validaEmail
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from front_pi.settings import API_URL

def login(request):

    if request.method == 'POST':
        email = request.POST['login-email']
        password = request.POST['login-password']
        
        if not email:
            mensagem = ['Você deve preencher o campo de e-mail']
            return render(request, 'auth/auth.html', {'messages': mensagem})
        if not validaEmail(email=email):
            mensagem = ['Você deve digitar um campo de e-mail válido']
            return render(request, 'auth/auth.html', {'messages': mensagem})
        if not password:
            mensagem = ['Você deve digitar uma senha.']
            return render(request, 'auth/auth.html', {'messages': mensagem})

        resp = requests.post(API_URL + '/api/auth/login/', {'email': email, 'password': password})
        if resp.json().get('user', False):
            return render(request, 'home/home.html')

        mensagem = ['Usuário ou senha inválidos']
        return render(request, 'auth/auth.html', {'messages': mensagem})
        
    else:
        form = LoginForm()
        
    return render(request, 'auth/auth.html', {'form': form})

@login_required
def home(request):
    return render(request, 'home/home.html', {'titulo': 'Home'})

def clientes(request):
    return render(request, 'clientes/clientes.html', {'titulo': 'Clientes'})

def cadastrar_clientes(request):
    return render(request, 'clientes/cadastrar_clientes.html', {'titulo': 'Cadastro de cliente'})


