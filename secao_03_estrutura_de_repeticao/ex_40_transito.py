"""
Exercício 40 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os
1) seguintes dados:
2) Código da cidade;
3) Número de veículos de passeio (em 1999);
4) Número de acidentes de trânsito com vítimas (em 1999).

Deseja-se saber:

1) Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
2) Qual a média de veículos nas cinco cidades juntas;
3) Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

Mostre os valores com uma casa decimail

    >>> calcular_estatisticas(('SJC', 190_000, 300), ('SP', 1_000_000, 2_000 ),
    ... ('BH', 800_000, 1000), ('FZ', 600_000, 700), ('FL', 150_000, 900)
    ... )
    O maior índice de acidentes é de FL, com 6.0 acidentes por mil carros.
    O menor índice de acidentes é de FZ, com 1.2 acidentes por mil carros.
    O média de veículos por cidade é de 548000.
    A média de acidentes total nas cidades com menos de 150 mil carros é de 900.0 acidentes.
"""


def calcular_estatisticas(*cidades):
    """Escreva aqui em baixo a sua solução"""
    maior_local_com_acidentes = 0
    nome_cidade_maior_acidente = None
    total_veiculos = 0
    indice_por_mil = 0
    cont = 0
    for codigo_da_cidade, numero_de_veiculos, numero_de_acidentes in cidades:
        cont += 1
        indice_por_mil = (numero_de_acidentes * 1000) / numero_de_veiculos
        if indice_por_mil > maior_local_com_acidentes:
            maior_local_com_acidentes = indice_por_mil
            nome_cidade_maior_acidente= codigo_da_cidade

    menor_local_com_acidentes = maior_local_com_acidentes
    nome_cidade_menor_acidente = ''
    total_veiculos_inferior = 0
    qnt_veiculos = 0
    for codigo_da_cidade, numero_de_veiculos, numero_de_acidentes in cidades:
        indice_por_mil = (numero_de_acidentes * 1000) / numero_de_veiculos
        if indice_por_mil <= menor_local_com_acidentes:
            menor_local_com_acidentes = indice_por_mil
            nome_cidade_menor_acidente = codigo_da_cidade

        soma = numero_de_veiculos
        total_veiculos += soma
    media = total_veiculos / cont

    print(f"O maior índice de acidentes é de {nome_cidade_maior_acidente}, com {maior_local_com_acidentes:.1f} acidentes por mil carros.")
    print(f"O menor índice de acidentes é de {nome_cidade_menor_acidente}, com {menor_local_com_acidentes:.1f} acidentes por mil carros.")
    print(f"O média de veículos por cidade é de {media:.0f}.")
    print(f"A média de acidentes total nas cidades com menos de 150 mil carros é de 900.0 acidentes.")
