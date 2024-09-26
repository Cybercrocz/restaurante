from django.shortcuts import render

from .models import Prato

def listar_pratos(request):
    pratos = Prato.objects.all()  # Pega todos os pratos do banco de dados
    return render(request, 'listar_pratos.html', {'pratos': pratos})  # Renderiza o template com os pratos

from django.shortcuts import render
from .models import Produto

def listar_produtos(request):
    produtos = Produto.objects.all()  # Obtém todos os produtos do banco de dados
    return render(request, 'pedidos/listar_produtos.html', {'produtos': produtos})
