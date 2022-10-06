import requests
from django.shortcuts import render
from toolbox import validaEmail
from front_pi.settings import API_URL
from .decorators import is_authenticated
from toolbox import validate_cpf, validate_cadastro_cliente
import logging

logger = logging.getLogger(__name__)

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
    
    # try:
    #     return render(request, 'clientes/clientes.html', {'titulo': 'Clientes', 'clientes': resp.json()})
    # except ValueError:
    #     return render(request, 'clientes/clientes.html', {'titulo': 'Clientes'}) 
    return render(request, 'clientes/clientes.html', {'titulo': 'Clientes', 'clientes': resp.json()})

@is_authenticated
def cadastrar_clientes(request):
    if request.method == 'POST':
        nome        = request.POST['cliente-nome']
        cpf         = request.POST['cliente-cpf'].replace('.', '').replace('-', '')
        email       = request.POST['cliente-email']
        telefone    = request.POST['cliente-telefone'].replace('(', '').replace(')', '').replace(' ', '').replace('-', '')
        endereco    = request.POST['cliente-endereco']

        validate = validate_cadastro_cliente(nome=nome, cpf=cpf, email=email, telefone=telefone, endereco=endereco)

        if not validate['status']:
            return render(request, 'clientes/cadastrar_clientes.html', {'titulo': 'Cadastro de cliente', 'messages': validate['message']}) 

        response = requests.post(API_URL + '/api/cliente/create/', headers={"Authorization": request.session["Authorization"]}, json=validate['data'])

        if response.status_code != 201:
            mensagem = ['Falha na realização do cadastro']
            return render(request, 'clientes/cadastrar_clientes.html', {'titulo': 'Cadastro de cliente', 'messages': mensagem}) 
                  
        mensagem = ['Cadastro realizado com sucesso']
        return render(request, 'clientes/cadastrar_clientes.html', {'titulo': 'Cadastro de cliente', 'messages': mensagem})

    return render(request, 'clientes/cadastrar_clientes.html', {'titulo': 'Cadastro de cliente'})

@is_authenticated
def detalhes_cliente(request, pk):

    response = requests.get(f'{API_URL}/api/cliente/{pk}', headers={'Authorization': request.session['Authorization']})

    return render(request, 'clientes/detalhes_cliente.html', {'titulo': 'Detalhes do cliente', 'cliente': response.json()})

@is_authenticated
def excluir_cliente(request, pk):

    response = requests.delete(f'{API_URL}/api/cliente/{pk}', headers={'Authorization': request.session['Authorization']})

    if response.status_code != 204:
        mensagem = ['Cadastro realizado com sucesso']
        return render(request, 'clientes/detalhes_cliente.html', {'titulo': 'Cadastro de cliente', 'messages': mensagem})
    
    mensagem = ['Cliente deletado com sucesso!']

    return render(request, 'clientes/detalhes_cliente.html', {'titulo': 'Detalhes do cliente', 'messages': mensagem})

@is_authenticated
def alterar_cliente(request, pk):


    if request.method == 'POST':
        nome        = request.POST['cliente-nome']
        cpf         = request.POST['cliente-cpf'].replace('.', '').replace('-', '')
        email       = request.POST['cliente-email']
        telefone    = request.POST['cliente-telefone'].replace('(', '').replace(')', '').replace(' ', '').replace('-', '')
        endereco    = request.POST['cliente-endereco']

        validate = validate_cadastro_cliente(nome=nome, cpf=cpf, email=email, telefone=telefone, endereco=endereco)

        if not validate['status']:
            return render(request, 'clientes/alterar_cliente.html', {'titulo': 'Cadastro de cliente', 'messages': validate['message']}) 

        cliente = validate['data']

        response = requests.put(f'{API_URL}/api/cliente/{pk}', headers={"Authorization": request.session["Authorization"]}, json=cliente)

        logger.warn(response.status_code)

        if response.status_code != 200:
            mensagem = ['Falha na realização do cadastro']
            return render(request, 'clientes/alterar_cliente.html', {'titulo': 'Cadastro de cliente', 'messages': mensagem}) 
                  
        mensagem = ['Cadastro realizado com sucesso']
        return render(request, 'clientes/alterar_cliente.html', {'titulo': 'Cadastro de cliente', 'messages': mensagem})

    
    response = requests.get(f'{API_URL}/api/cliente/{pk}', headers={'Authorization': request.session['Authorization']})

    cliente = response.json()

    logger.warn(cliente)
    return render(request, 'clientes/alterar_cliente.html', {'titulo': 'Alterar cliente', 'cliente': cliente})

def produtos(request):
    return render(request, 'produtos/produtos.html', {'titulo': 'Produtos'})

def cadastrar_produtos(request):
    return render(request, 'produtos/cadastrar_produtos.html', {'titulo': 'Cadastro de Produto'})


