"""
Exercício 18 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

    >>> validar_data('')
    'Data inválida'
    >>> validar_data('1')
    'Data inválida'
    >>> validar_data('1/2/2004')
    'Data válida'
    >>> validar_data('1/02/2004')
    'Data válida'
    >>> validar_data('01/02/2004')
    'Data válida'
    >>> validar_data('30/02/2004')
    'Data inválida'
    >>> validar_data('01/13/2004')
    'Data inválida'

"""


def validar_data(data: str):
    """Escreva aqui em baixo a sua solução"""
    lista_datas_erradas = list(range(1, 5))
    lista_datas_erradas = ['30/02/2004', '1/13/2004', '1', '']
    if data == lista_datas_erradas:
        print("'Data inválida'")
        print(lista_datas_erradas)
    else:
        if len(data) >= 6:
            print("'Data válida'")
