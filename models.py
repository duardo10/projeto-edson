import os
from django.conf import settings
from django.http import JsonResponse
from django.db import models
from django.urls import path

# Configurações do Django
DEBUG = True
SECRET_KEY = 'YOUR_SECRET_KEY'  # Certifique-se de definir uma chave secreta forte em um ambiente de produção
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ROOT_URLCONF=__name__,
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    },
    STATIC_URL='/static/',
)

# Definição do modelo Cliente
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    data_inicio_divida = models.DateField()
    data_fim_divida = models.DateField()

# Função de visualização (view) para listar os clientes
def cliente_list(request):
    clientes = Cliente.objects.all().values()
    return JsonResponse(list(clientes), safe=False)

# Função de visualização (view) para criar um novo cliente
def create_cliente(request):
    data = request.POST
    new_cliente = Cliente.objects.create(
        nome=data['name'],
        cidade=data['city'],
        data_inicio_divida=data['debt-start'],
        data_fim_divida=data['debt-end']
    )
    return JsonResponse({
        'id': new_cliente.id,
        'name': new_cliente.nome,
        'city': new_cliente.cidade,
        'debtStart': new_cliente.data_inicio_divida,
        'debtEnd': new_cliente.data_fim_divida
    })

# Definição das URLs
urlpatterns = [
    path('api/clientes', cliente_list),
    path('api/clientes/create', create_cliente)
]

# Execução do servidor de desenvolvimento do Django
if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line([os.path.abspath(__file__), 'runserver'])
