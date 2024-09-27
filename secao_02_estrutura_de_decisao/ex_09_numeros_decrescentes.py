"""
Exercício 09 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia três números e mostre-os em ordem decrescente.

    >>> ordenar_decrescente(2, 3, 5)
    5, 3, 2
    >>> ordenar_decrescente(10, 5.55, 7)
    10, 7, 5.55
    >>> ordenar_decrescente(20, 30, 17.62)
    30, 20, 17.62
    >>> ordenar_decrescente(7, 1, 15)
    15, 7, 1

"""


def ordenar_decrescente(x, y, z):
    """Escreva aqui em baixo a sua solução"""
    if (x < z) and (x < y) and (z > y):
        print(z, y, x, sep=", ")
    elif (x > z) and (x > y) and (z > y):
        print(x, z, y, sep=", ")
    elif (x < y) and (x > z) and (y > x):
        print(y, x, z, sep=", ")
    elif (x < z) and (x > y) and (z > y):
        print(z, x, y, sep=", ")
