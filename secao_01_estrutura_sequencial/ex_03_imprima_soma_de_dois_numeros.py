"""
Exercício 03 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça dois números inteiros e imprima a soma.

    >>> from secao_01_estrutura_sequencial import ex_03_imprima_soma_de_dois_numeros
    >>> numeros =['42', '43']
    >>> ex_03_imprima_soma_de_dois_numeros.input = lambda k: numeros.pop()
    >>> ex_03_imprima_soma_de_dois_numeros.imprima_a_soma_de_dois_numeros()
    A soma dos dois números informados é 85

"""


def imprima_a_soma_de_dois_numeros():
    """Escreva aqui em baixo a sua solução"""
    primeiro_numero = int(input("Primeiro número: "))
    segundo_numero = int(input("Segundo número: "))
    soma = primeiro_numero+segundo_numero
    print("A soma dos dois números informados é",soma, sep=" ")
