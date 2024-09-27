"""
Exercício 25 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma
varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média
calculada.

Mostre a média de idade com uma casa decimal.

    >>> classifcar_turma(20)
    'A turma é jovem, pois a média é de 20.0 anos'
    >>> classifcar_turma(20, 30)
    'A turma é jovem, pois a média é de 25.0 anos'
    >>> classifcar_turma(20, 30, 95)
    'A turma é adulta, pois a média é de 48.3 anos'
    >>> classifcar_turma(20, 30, 95, 95)
    'A turma é idosa, pois a média é de 60.0 anos'
    >>> classifcar_turma(20, 30, 95, 95, 95)
    'A turma é idosa, pois a média é de 67.0 anos'

"""


def classifcar_turma(*idades) -> str:
    """Escreva aqui em baixo a sua solução"""
    cont = 0
    i = 0
    media_anos = 0
    anos = 0
    if len(idades) == 5:
        cont = 5
    elif len(idades) == 4:
        cont = 4
    elif len(idades) == 3:
        cont = 3
    elif len(idades) == 2:
        cont = 2
    elif len(idades) == 1:
        cont = 1
    while i < cont:
        anos += idades[i]
        i += 1
        media_anos = anos / i
    if media_anos <= 30:
        print(f"'A turma é jovem, pois a média é de {media_anos:.1f} anos'")
    elif 30 < media_anos < 60:
        print(f"'A turma é adulta, pois a média é de {media_anos:.1f} anos'")
    else:
        print(f"'A turma é idosa, pois a média é de {media_anos:.1f} anos'")
