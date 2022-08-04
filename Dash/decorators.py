# Decorador são formas de alterar o comportamento de uma função....
# por exemplo retornar tudo em maiúscula ou minúscula

# 1 Definindo variáveis como funções


def soma_um(numero):
    return numero +1

f1 = soma_um
f1(10) #podemos definir variáveis como funções

# 2 Definindo funções dentro de outras funções
def soma_um(numero):
    def adiciona_um(numero):
        return numero +1
    return adiciona_um(numero)

soma_um(4)

# 3 Passando funções como argumentos de outras funções
def soma_um(numero):
    return numero +1

def function_call(function):
    numero_to_add = 5
    return function(numero_to_add)

function_call(soma_um)

# 4 Funções retornando outras funções
def funcao_ola():
    def diga_oi():
        return 'Hi'
    return diga_oi()

hello = funcao_ola
hello()

# Função para alterar funções que retornam strings

def decorador_maiusculo(function):
    def wrapper():
        func = function()
        cria_maiusculo = func.upper()
        return cria_maiusculo
    return wrapper

def diga_oi():
    return 'Olá cara'

funcao_decorada = decorador_maiusculo(diga_oi)
funcao_decorada()

# Ou posso fazer
@decorador_maiusculo
def diga_oi():
    return 'Olá cara'
diga_oi()