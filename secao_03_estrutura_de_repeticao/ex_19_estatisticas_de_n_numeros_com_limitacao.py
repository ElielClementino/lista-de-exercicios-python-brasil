"""
Exercício 19 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

    >>> calcular_estatisticas()
    'Maior valor: não existe. Menor valor: não existe. Soma: 0'
    >>> calcular_estatisticas(1)
    'Maior valor: 1. Menor valor: 1. Soma: 1'
    >>> calcular_estatisticas(1, 2)
    'Maior valor: 2. Menor valor: 1. Soma: 3'
    >>> calcular_estatisticas(1, 2, -1)
    'Somente números de 0 a 1000 são permitidos'
    >>> calcular_estatisticas(1, 2, -10)
    'Somente números de 0 a 1000 são permitidos'
    >>> calcular_estatisticas(1, 2, 1001)
    'Somente números de 0 a 1000 são permitidos'
    >>> calcular_estatisticas(1, 2, 1198)
    'Somente números de 0 a 1000 são permitidos'

"""


def calcular_estatisticas(*numeros) -> str:
    """Escreva aqui em baixo a sua solução"""
    cont = 6
    if numeros[0] > 1000 or numeros[0] < 0 or numeros[1] > 1000 or numeros[1] < 0 or numeros[2] > 1000 or numeros[2] < 0:
        print("'Somente números de 0 a 1000 são permitidos'")
    else:
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
