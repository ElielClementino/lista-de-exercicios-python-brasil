"""
Exercício 08 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão
é sempre pelo mais barato.
Mostrar o resultado com duas casas decimais

    >>> decidir_melhor_produto(2, 3, 5)
    Melhor produto custa R$ 2.00
    >>> decidir_melhor_produto(10, 5.55, 7)
    Melhor produto custa R$ 5.55
    >>> decidir_melhor_produto(20, 30, 17.62)
    Melhor produto custa R$ 17.62
    >>> decidir_melhor_produto(7, 1, 15)
    Melhor produto custa R$ 1.00

"""


def decidir_melhor_produto(x, y, z):
    """Escreva aqui em baixo a sua solução"""
    decidir_melhor_produto()
    p1 = x
    p2 = y
    p3 = z
    if x < y < z:
        print(f"Melhor produto custa R$ {x:.2f}")
    elif x > y < z:
        print(f"Melhor produto custa R$ {y:.2f}")
    elif x < y > z:
        print(f"Melhor produto custa R$ {z:.2f}")
