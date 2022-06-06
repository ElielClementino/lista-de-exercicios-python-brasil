"""
Exercício 04 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a
população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o
número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas
de crescimento.

    >>> calcular_ano_ultrapassagem_populacional()
    'População de A, depois de 63 ano(s) será de 515033 pessoas, superando a de B, que será de 510964 pessoas'


"""


def calcular_ano_ultrapassagem_populacional() -> str:
    """Escreva aqui em baixo a sua solução"""
    populacao_a = 80_000
    populacao_b = 200_000
    pop_inicial_a = populacao_a
    pop_inicial_b = populacao_b
    cresc_a = 1.03
    cresc_b = 1.015
    anos = 0
    while populacao_a < populacao_b:
        anos += 1
        populacao_a = pop_inicial_a * (cresc_a ** anos)
        populacao_b = pop_inicial_b * (cresc_b ** anos)
        populacao_a = int(populacao_a)
        populacao_b = int(populacao_b)

    print(f"'População de A, depois de {anos} ano(s) será de {populacao_a} pessoas, superando a de B, que será de {populacao_b} pessoas'")
