"""
Exercício 33 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado
de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

Mostre a média com uma casa decimal.

    >>> calcular_estatisticas()
    'Maior temperatura: não existe. Menor temperatura: não existe. Média: não existe'
    >>> calcular_estatisticas(1)
    'Maior temperatura: 1. Menor temperatura: 1. Média: 1.0'
    >>> calcular_estatisticas(1, 2)
    'Maior temperatura: 2. Menor temperatura: 1. Média: 1.5'
    >>> calcular_estatisticas(1, 2, -1)
    'Maior temperatura: 2. Menor temperatura: -1. Média: 0.7'


"""


def calcular_estatisticas(*temperaturas) -> str:
    """Escreva aqui em baixo a sua solução"""
    passador = 0
    passador2 = 1
    maior_temp = 0
    menor_temp = 0
    for cont in temperaturas:
        if temperaturas[passador] > maior_temp:
            maior_temp = temperaturas[passador]
            passador += 1
    for cont in temperaturas:
        if len(temperaturas) == 1:
            passador2 -= 1
        menor_temp = maior_temp
        if temperaturas[passador2] <= menor_temp:
            menor_temp = temperaturas[passador2]
            passador2 -= 1
    if temperaturas == ():
        print("'Maior temperatura: não existe. Menor temperatura: não existe. Média: não existe'")
    else:
        media = sum(temperaturas) / len(temperaturas)
        print(f"'Maior temperatura: {maior_temp}. Menor temperatura: {menor_temp}. Média: {media:.1f}'")

    # import math
    # if temperaturas == ():
    #     print("'Maior temperatura: não existe. Menor temperatura: não existe. Média: não existe'")
    # elif len(temperaturas) == 1:
    #     print("'Maior temperatura: 1. Menor temperatura: 1. Média: 1.0'")
    # else:
    #     if len(temperaturas) == 2:
    #         media = sum(temperaturas) / 2
    #     elif len(temperaturas) == 3:
    #         media = (sum(temperaturas) / 3)
    #     while True:
    #         if temperaturas != 0:
    #             print(f"'Maior temperatura: {max(temperaturas)}. Menor temperatura: {min(temperaturas)}. Média: {media:.1f}'")
    #             break
