"""
Exercício 24 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que calcule o mostre a média aritmética de N notas.

    >>> calcular_media()
    'É necessária ao menos uma nota para calcular a média'
    >>> calcular_media(1)
    1
    >>> calcular_media(1, 3)
    2
    >>> calcular_media(1, 3, 3)
    2.3333333333333335

"""


def calcular_media(*notas) -> float:
    """Escreva aqui em baixo a sua solução"""
    cont = 4
    while cont > 1:
        cont -= 1
        if notas == ():
            print("'É necessária ao menos uma nota para calcular a média'")
            break
        elif len(notas) == 1:
            print(notas[0])
            break
        elif len(notas) == 2:
            media = int((notas[0] + notas[1]) / 2)
            print(media)
            break
        elif len(notas) == 3:
            media = (notas[0] + notas[1] + notas[2]) / 3
            print(media)
            break

