"""
Exercício 01 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo
até que o usuário informe um valor válido.

    >>> from secao_03_estrutura_de_repeticao import ex_01_numero_valido
    >>> ex_01_numero_valido.input = lambda k: '0'
    >>> ex_01_numero_valido.obter_numero_valido()
    0
    >>> entradas = ['1', 'a']
    >>> ex_01_numero_valido.input = lambda k: entradas.pop()
    >>> ex_01_numero_valido.obter_numero_valido()
    Número inválido: a
    1
    >>> entradas = ['0', 'a', '-1']
    >>> ex_01_numero_valido.input = lambda k: entradas.pop()
    >>> ex_01_numero_valido.obter_numero_valido()
    Número inválido: -1
    Número inválido: a
    0
    >>> entradas = ['10', 'a', '-1', '11']
    >>> ex_01_numero_valido.input = lambda k: entradas.pop()
    >>> ex_01_numero_valido.obter_numero_valido()
    Número inválido: 11
    Número inválido: -1
    Número inválido: a
    10


"""


def obter_numero_valido():
    """Escreva aqui em baixo a sua solução"""
    while True:
        nota = input("Digite uma nota entre 0 e 10: ")
        if nota.isnumeric() == False:
            print(f"Número inválido: {nota}")
        else:
            nota = int(nota)
            if nota < 0 or nota > 10:
                print(f"Número inválido: {nota}")
            else:
                print(f"{nota}")
                break
    # while True:
    #     numero = int(input("Digite um número de 0 a 10"))
    #     if 1 <= numero <= 10:
    #         print(numero)
    #         break
    #     else:
    #         print(f"Número inválido: {numero}")
