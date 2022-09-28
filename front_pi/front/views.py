import requests
from django.shortcuts import render
from .validators import validaEmail
from front_pi.settings import API_URL
from .decorators import is_authenticated

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
            request.session["Authorization"] = 'Bearer ' + resp.json().get('access')
            return render(request, 'home/home.html')
        mensagem = ['Usuário ou senha inválidos']
        return render(request, 'auth/auth.html', {'messages': mensagem})
        
    return render(request, 'auth/auth.html')

@is_authenticated
def home(request):
    return render(request, 'home/home.html', {'titulo': 'Home'})

@is_authenticated
def clientes(request):
    resp = requests.get(API_URL + '/api/cliente/list/', headers={'Authorization': request.session['Authorization']})
    return render(request, 'clientes/clientes.html', {'titulo': 'Clientes', 'clientes': resp.json()})

@is_authenticated
def cadastrar_clientes(request):
    if request.method == 'POST':
        nome        = request.POST['cliente-nome']
        cpf         = request.POST['cliente-cpf']
        email       = request.POST['cliente-email']
        telefone    = request.POST['cliente-telefone']
        cidade      = request.POST['cliente-cidade']
        cep         = request.POST['cliente-cep']

        if not nome:
            mensagem = ['Você deve preencher o campo de nome']
            return render(request, 'clientes/cadastrar_clientes.html', {'messages': mensagem})
        if not cpf:
            mensagem = ['Você deve preencher o campo de CPF']
            return render(request, 'clientes/cadastrar_clientes.html', {'messages': mensagem})
        if not email:
            mensagem = ['Você deve preencher o campo de nome']
            return render(request, 'clientes/cadastrar_clientes.html', {'messages': mensagem})    

    return render(request, 'clientes/cadastrar_clientes.html', {'titulo': 'Cadastro de cliente'})

def produtos(request):
    return render(request, 'produtos/produtos.html', {'titulo': 'Produtos'})

def cadastrar_produtos(request):
    return render(request, 'produtos/cadastrar_produtos.html', {'titulo': 'Cadastro de Produto'})


