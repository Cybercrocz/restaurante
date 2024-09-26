from django.contrib import admin
from .models import Produto, Pedido, Cliente

# Registrando os modelos no admin
admin.site.register(Produto)
admin.site.register(Pedido)
admin.site.register(Cliente)
