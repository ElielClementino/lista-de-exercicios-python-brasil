"""
Exercício 28 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há
limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um
desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo
usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total,
tipo de pagamento, valor do desconto e valor a pagar.

Mostre o restultado com duas casas decimais

    >>> calcular_preco_da_carne('Filé Duplo', 2, 'dinheiro')
    '2 kg de Filé Duplo a R$ 4.90/kg saem a R$ 9.80. Não há desconto, pagamento feito com dinheiro'
    >>> calcular_preco_da_carne('Filé Duplo', 4, 'cartão tabajara')
    '4 kg de Filé Duplo a R$ 4.90/kg saem a R$ 19.60. Com desconto de 5% pelo pagamento feito com cartão tabajara, fica R$ 18.62'
    >>> calcular_preco_da_carne('Filé Duplo', 6, 'pix')
    '6 kg de Filé Duplo a R$ 5.80/kg saem a R$ 34.80. Não há desconto, pagamento feito com pix'
    >>> calcular_preco_da_carne('Filé Duplo', 8, 'cartão tabajara')
    '8 kg de Filé Duplo a R$ 5.80/kg saem a R$ 46.40. Com desconto de 5% pelo pagamento feito com cartão tabajara, fica R$ 44.08'
    >>> calcular_preco_da_carne('Alcatra', 2, 'dinheiro')
    '2 kg de Alcatra a R$ 5.90/kg saem a R$ 11.80. Não há desconto, pagamento feito com dinheiro'
    >>> calcular_preco_da_carne('Alcatra', 4, 'cartão tabajara')
    '4 kg de Alcatra a R$ 5.90/kg saem a R$ 23.60. Com desconto de 5% pelo pagamento feito com cartão tabajara, fica R$ 22.42'
    >>> calcular_preco_da_carne('Alcatra', 6, 'dinheiro')
    '6 kg de Alcatra a R$ 6.80/kg saem a R$ 40.80. Não há desconto, pagamento feito com dinheiro'
    >>> calcular_preco_da_carne('Alcatra', 8, 'cartão tabajara')
    '8 kg de Alcatra a R$ 6.80/kg saem a R$ 54.40. Com desconto de 5% pelo pagamento feito com cartão tabajara, fica R$ 51.68'
    >>> calcular_preco_da_carne('Picanha', 2, 'dinheiro')
    '2 kg de Picanha a R$ 6.90/kg saem a R$ 13.80. Não há desconto, pagamento feito com dinheiro'
    >>> calcular_preco_da_carne('Picanha', 4, 'cartão tabajara')
    '4 kg de Picanha a R$ 6.90/kg saem a R$ 27.60. Com desconto de 5% pelo pagamento feito com cartão tabajara, fica R$ 26.22'
    >>> calcular_preco_da_carne('Picanha', 6, 'dinheiro')
    '6 kg de Picanha a R$ 7.80/kg saem a R$ 46.80. Não há desconto, pagamento feito com dinheiro'
    >>> calcular_preco_da_carne('Picanha', 8, 'cartão tabajara')
    '8 kg de Picanha a R$ 7.80/kg saem a R$ 62.40. Com desconto de 5% pelo pagamento feito com cartão tabajara, fica R$ 59.28'
    
"""


def calcular_preco_da_carne(tipo_de_carne: str, kilos_de_carne: int, forma_de_pagamento: str) -> str:
    """Escreva aqui em baixo a sua solução"""
    valor_file_ate_5kg = 4.90
    valor_alcatra_ate_5kg = 5.90
    valor_picanha_ate_5kg = 6.90

    valor_file_mais_5kg = 5.80
    valor_alcatra_mais_5kg = 6.80
    valor_picanha_mais_5kg = 7.80
    desconto = 0
    # area do filé duplo
    if tipo_de_carne == 'Filé Duplo' and kilos_de_carne <= 5 and forma_de_pagamento == 'cartão tabajara':
        desconto = 0.05
        valor_sem_desconto = kilos_de_carne * valor_file_ate_5kg
        valor_com_desconto = valor_sem_desconto * desconto
        valor_descontado = valor_sem_desconto - valor_com_desconto
        print(f"'{kilos_de_carne} kg de Filé Duplo a R$ 4.90/kg saem a R$ {valor_sem_desconto:.2f}. Com desconto de 5% pelo pagamento feito com cartão tabajara, fica R$ {valor_descontado:.2f}'")
    elif tipo_de_carne == 'Filé Duplo' and kilos_de_carne <= 5 and forma_de_pagamento != 'cartão tabajara':
        valor_sem_desconto = kilos_de_carne * valor_file_ate_5kg
        print(f"'{kilos_de_carne} kg de Filé Duplo a R$ 4.90/kg saem a R$ {valor_sem_desconto:.2f}. Não há desconto, pagamento feito com {forma_de_pagamento}'")
    if tipo_de_carne == 'Filé Duplo' and kilos_de_carne > 5 and forma_de_pagamento == 'cartão tabajara':
        desconto = 0.05
        valor_sem_desconto = kilos_de_carne * valor_file_mais_5kg
        valor_com_desconto = valor_sem_desconto * desconto
        valor_descontado = valor_sem_desconto - valor_com_desconto
        print(f"'{kilos_de_carne} kg de Filé Duplo a R$ 5.80/kg saem a R$ {valor_sem_desconto:.2f}. Com desconto de 5% pelo pagamento feito com cartão tabajara, fica R$ {valor_descontado:.2f}'")
    elif tipo_de_carne == 'Filé Duplo' and kilos_de_carne > 5 and forma_de_pagamento != 'cartão tabajara':
        valor_sem_desconto = kilos_de_carne * valor_file_mais_5kg
        print(f"'{kilos_de_carne} kg de Filé Duplo a R$ 5.80/kg saem a R$ {valor_sem_desconto:.2f}. Não há desconto, pagamento feito com {forma_de_pagamento}'")
    # area da alcatra
    if tipo_de_carne == 'Alcatra' and kilos_de_carne <= 5 and forma_de_pagamento == 'cartão tabajara':
        desconto = 0.05
        valor_sem_desconto = kilos_de_carne * valor_alcatra_ate_5kg
        valor_com_desconto = valor_sem_desconto * desconto
        valor_descontado = valor_sem_desconto - valor_com_desconto
        print(f"'{kilos_de_carne} kg de Alcatra a R$ 5.90/kg saem a R$ {valor_sem_desconto:.2f}. Com desconto de 5% pelo pagamento feito com cartão tabajara, fica R$ {valor_descontado:.2f}'")
    elif tipo_de_carne == 'Alcatra' and kilos_de_carne <= 5 and forma_de_pagamento != 'cartão tabajara':
        valor_sem_desconto = kilos_de_carne * valor_alcatra_ate_5kg
        print(f"'{kilos_de_carne} kg de Alcatra a R$ 5.90/kg saem a R$ {valor_sem_desconto:.2f}. Não há desconto, pagamento feito com {forma_de_pagamento}'")
    if tipo_de_carne == 'Alcatra' and kilos_de_carne > 5 and forma_de_pagamento == 'cartão tabajara':
        desconto = 0.05
        valor_sem_desconto = kilos_de_carne * valor_alcatra_mais_5kg
        valor_com_desconto = valor_sem_desconto * desconto
        valor_descontado = valor_sem_desconto - valor_com_desconto
        print(f"'{kilos_de_carne} kg de Alcatra a R$ 6.80/kg saem a R$ {valor_sem_desconto:.2f}. Com desconto de 5% pelo pagamento feito com cartão tabajara, fica R$ {valor_descontado:.2f}'")
    elif tipo_de_carne == 'Alcatra' and kilos_de_carne > 5 and forma_de_pagamento != 'cartão tabajara':
        valor_sem_desconto = kilos_de_carne * valor_alcatra_mais_5kg
        print(f"'{kilos_de_carne} kg de Alcatra a R$ 6.80/kg saem a R$ {valor_sem_desconto:.2f}. Não há desconto, pagamento feito com {forma_de_pagamento}'")
# area da picanha
    if tipo_de_carne == 'Picanha' and kilos_de_carne <= 5 and forma_de_pagamento == 'cartão tabajara':
        desconto = 0.05
        valor_sem_desconto = kilos_de_carne * valor_picanha_ate_5kg
        valor_com_desconto = valor_sem_desconto * desconto
        valor_descontado = valor_sem_desconto - valor_com_desconto
        print(f"'{kilos_de_carne} kg de Picanha a R$ 6.90/kg saem a R$ {valor_sem_desconto:.2f}. Com desconto de 5% pelo pagamento feito com cartão tabajara, fica R$ {valor_descontado:.2f}'")
    elif tipo_de_carne == 'Picanha' and kilos_de_carne <= 5 and forma_de_pagamento != 'cartão tabajara':
        valor_sem_desconto = kilos_de_carne * valor_picanha_ate_5kg
        print(f"'{kilos_de_carne} kg de Picanha a R$ 6.90/kg saem a R$ {valor_sem_desconto:.2f}. Não há desconto, pagamento feito com {forma_de_pagamento}'")
    if tipo_de_carne == 'Picanha' and kilos_de_carne > 5 and forma_de_pagamento == 'cartão tabajara':
        desconto = 0.05
        valor_sem_desconto = kilos_de_carne * valor_picanha_mais_5kg
        valor_com_desconto = valor_sem_desconto * desconto
        valor_descontado = valor_sem_desconto - valor_com_desconto
        print(f"'{kilos_de_carne} kg de Picanha a R$ 7.80/kg saem a R$ {valor_sem_desconto:.2f}. Com desconto de 5% pelo pagamento feito com cartão tabajara, fica R$ {valor_descontado:.2f}'")
    elif tipo_de_carne == 'Picanha' and kilos_de_carne > 5 and forma_de_pagamento != 'cartão tabajara':
        valor_sem_desconto = kilos_de_carne * valor_picanha_mais_5kg
        print(f"'{kilos_de_carne} kg de Picanha a R$ 7.80/kg saem a R$ {valor_sem_desconto:.2f}. Não há desconto, pagamento feito com {forma_de_pagamento}'")
