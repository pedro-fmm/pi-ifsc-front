from django.urls import path
from .views import login, home, clientes, cadastrar_clientes

app_name = 'front'

"""
Urls do app front.
"""

urlpatterns = [
    path('login/', login, name='login'),
    path('home/', home, name='home'),
    path('clientes/', clientes, name='clientes'),
    path('clientes/cadastro/', cadastrar_clientes, name='cadastrar_clientes')
]