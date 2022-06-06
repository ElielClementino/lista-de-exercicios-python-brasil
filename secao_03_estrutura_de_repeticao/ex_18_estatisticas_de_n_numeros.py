"""
Exercício 18 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

    >>> calcular_estatisticas()
    'Maior valor: não existe. Menor valor: não existe. Soma: 0'
    >>> calcular_estatisticas(1)
    'Maior valor: 1. Menor valor: 1. Soma: 1'
    >>> calcular_estatisticas(1, 2)
    'Maior valor: 2. Menor valor: 1. Soma: 3'
    >>> calcular_estatisticas(1, 2, -1)
    'Maior valor: 2. Menor valor: -1. Soma: 2'

"""


def calcular_estatisticas(*numeros) -> str:
    """Escreva aqui em baixo a sua solução"""
    cont = 4
    while cont > 1:
        cont -= 1
        soma = 0
        if numeros == ():
            print("'Maior valor: não existe. Menor valor: não existe. Soma: 0'")
            break
        elif len(numeros) == 1:
            print(f"'Maior valor: {max(numeros)}. Menor valor: 1. Soma: {min(numeros)}'")
            break
        elif len(numeros) == 2:
            soma = numeros[0] + numeros[1]
            print(f"'Maior valor: {max(numeros)}. Menor valor: {min(numeros)}. Soma: {soma}'")
            break
        elif len(numeros) == 3:
            soma = numeros[0] + numeros[1] + numeros[2]
            print(f"'Maior valor: {max(numeros)}. Menor valor: {min(numeros)}. Soma: {soma}'")
            break
