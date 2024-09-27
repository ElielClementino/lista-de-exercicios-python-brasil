"""
Exercício 43 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

O cardápio de uma lanchonete é o seguinte:

Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00

Faça um programa que receba os itens pedidos e as quantidades desejadas.
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido e quantidade de itens
comprados.


    >>> fechar_conta()
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          0 |       0.00 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          1 |       1.20 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          1 |       1.20 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          3 |       3.60 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          5 |       6.20 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |          8 |      10.70 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3), ('103', 4))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    | Hamburger        | 103    | 1.20                |          4 |       4.80 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |         12 |      15.50 |
    -----------------------------------------------------------------------------

    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3), ('103', 4), ('104', 5))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    | Hamburger        | 103    | 1.20                |          4 |       4.80 |
    | Cheeseburger     | 104    | 1.30                |          5 |       6.50 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |         17 |      22.00 |
    -----------------------------------------------------------------------------
    >>> fechar_conta(('100', 1), ('100', 2), ('101', 2), ('102', 3), ('103', 4), ('105', 6))
    _____________________________________________________________________________
    |                              RESUMO DA CONTA                              |
    |---------------------------------------------------------------------------|
    | Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |
    | Cachorro Quente  | 100    | 1.20                |          3 |       3.60 |
    | Bauru Simples    | 101    | 1.30                |          2 |       2.60 |
    | Bauru com Ovo    | 102    | 1.50                |          3 |       4.50 |
    | Hamburger        | 103    | 1.20                |          4 |       4.80 |
    | Refrigerante     | 105    | 1.00                |          6 |       6.00 |
    |---------------------------------------------------------------------------|
    | Total Geral:                                    |         18 |      21.50 |
    -----------------------------------------------------------------------------

"""


def fechar_conta(*itens):
    """Escreva aqui em baixo a sua solução"""
    qnt_cachorro = 0
    qnt_bauru_simples = 0
    qnt_bauru_com_ovo = 0
    qnt_hamburger = 0
    qnt_cheeseburger = 0
    qnt_refrigerante = 0
    valor_cachorro = 1.20
    valor_bauru_simples = 1.30
    valor_bauru_com_ovo = 1.50
    valor_hamburger = 1.20
    valor_cheeseburger = 1.30
    valor_refrigerante = 1.00
    lista_codigos = []
    lista_quantidade = []
    for codigo, quantidade in itens:
        lista_codigos.append(codigo)
        lista_quantidade.append(quantidade)
    print('_____________________________________________________________________________')
    print('|                              RESUMO DA CONTA                              |')
    print('|---------------------------------------------------------------------------|')
    print('| Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |')
    for cont in range(0, len(lista_codigos)):
        if lista_codigos[cont] == '100':
            qnt_cachorro += lista_quantidade[cont]
        if lista_codigos[cont] == '101':
            qnt_bauru_simples += lista_quantidade[cont]
        if lista_codigos[cont] == '102':
            qnt_bauru_com_ovo += lista_quantidade[cont]
        if lista_codigos[cont] == '103':
            qnt_hamburger += lista_quantidade[cont]
        if lista_codigos[cont] == '104':
            qnt_cheeseburger += lista_quantidade[cont]
        if lista_codigos[cont] == '105':
            qnt_refrigerante += lista_quantidade[cont]

    valor_cachorro *= qnt_cachorro
    valor_bauru_simples *= qnt_bauru_simples
    valor_bauru_com_ovo *= qnt_bauru_com_ovo
    valor_hamburger *= qnt_hamburger
    valor_cheeseburger *= qnt_cheeseburger
    valor_refrigerante *= qnt_refrigerante

    qnt_total = qnt_cachorro + qnt_bauru_simples + qnt_bauru_com_ovo + qnt_hamburger + qnt_cheeseburger + qnt_refrigerante
    valor_final = valor_cachorro + valor_bauru_simples + valor_bauru_com_ovo + valor_hamburger + valor_cheeseburger + valor_refrigerante

    if qnt_cachorro >= 1:
        print(f'| Cachorro Quente  | 100    | 1.20                |          {qnt_cachorro} |       {valor_cachorro:.2f} |')
    if qnt_bauru_simples >= 1:
        print(f'| Bauru Simples    | 101    | 1.30                |          {qnt_bauru_simples} |       {valor_bauru_simples:.2f} |')
    if qnt_bauru_com_ovo >= 1:
        print(f'| Bauru com Ovo    | 102    | 1.50                |          {qnt_bauru_com_ovo} |       {valor_bauru_com_ovo:.2f} |')
    if qnt_hamburger >= 1:
        print(f'| Hamburger        | 103    | 1.20                |          {qnt_hamburger} |       {valor_hamburger:.2f} |')
    if qnt_cheeseburger >= 1:
        print(f'| Cheeseburger     | 104    | 1.30                |          {qnt_cheeseburger} |       {valor_cheeseburger:.2f} |')
    if qnt_refrigerante >= 1:
        print(f'| Refrigerante     | 105    | 1.00                |          {qnt_refrigerante} |       {valor_refrigerante:.2f} |')
    print('|---------------------------------------------------------------------------|')
    print(f'| Total Geral:                                    |{qnt_total:>11} |{valor_final:>11.2f} |')
    print('-----------------------------------------------------------------------------')
    # lista_codigos = []
    # lista_quantidade = []
    # quantidade = 0
    # total = 0
    # valor = 0
    # produtos = ['Cachorro Quente', 'Bauru Simples', 'Bauru com ovo', 'Hambúrguer', 'Cheeseburger', 'Refrigerantes']
    # valores = [1.20, 1.30, 1.50, 1.20, 1.30, 1.00]
    # print("_____________________________________________________________________________")
    # print("|                              RESUMO DA CONTA                              |")
    # print("|---------------------------------------------------------------------------|")
    # print("| Epecificação     | Código | Preço Unitário (R$) | Quantidade | Total (R$) |")
    # for codigo, quantidade in itens:
    #     lista_codigos.append(codigo)
    #     lista_quantidade.append(quantidade)
    # if itens != ():
    #     for cont in range(0, len(itens)):
    #         quantidade = lista_quantidade[cont]
    #         valor = valores[cont]
    #         total = lista_quantidade[cont] * valores[cont]
    #         print(f"| {produtos[cont]}  | {lista_codigos[cont]}    | {valores[cont]:.2f}                |          {lista_quantidade[cont]} |       {total:.2f} |")
    # total = quantidade * valor
    # print("|---------------------------------------------------------------------------|")
    # print(f"| Total Geral:                                    |          {quantidade} |       {total:.2f} |")
    # print("-----------------------------------------------------------------------------")
