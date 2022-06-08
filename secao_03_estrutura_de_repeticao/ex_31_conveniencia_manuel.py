"""
Exercício 31 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

FO Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de
valores referentes aos preços das mercadorias.
Um valor zero deve ser informado pelo operador para indicar o final da compra.
Um valor -1 deve ser informado pelo operador para finalizar o programas
O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então
calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial,
para registrar a próxima compra.

    >>> from secao_03_estrutura_de_repeticao import ex_31_conveniencia_manuel
    >>> entradas = ['-1']  # Encerrando o programa sem nenhuma compra
    >>> ex_31_conveniencia_manuel.input = lambda k: entradas.pop()
    >>> ex_31_conveniencia_manuel.rodar_programa_de_caixa()
    Lojas Tabajara
    -------------------
    Programa encerrado!
    >>> entradas = ['2.00', '-1', '1.99']  # Compra de apenas um produto
    >>> ex_31_conveniencia_manuel.input = lambda k: entradas.pop()
    >>> ex_31_conveniencia_manuel.rodar_programa_de_caixa()
    Lojas Tabajara
    Total     : R$   1.99
    Dinheiro  : R$   2.00
    Troco     : R$   0.01
    -------------------
    Programa encerrado!
    >>> entradas = ['5.00', '-1', '1.99', '1.99']  # Compra de dois produtos
    >>> ex_31_conveniencia_manuel.input = lambda k: entradas.pop()
    >>> ex_31_conveniencia_manuel.rodar_programa_de_caixa()
    Lojas Tabajara
    Total     : R$   3.98
    Dinheiro  : R$   5.00
    Troco     : R$   1.02
    -------------------
    Programa encerrado!
    >>> entradas = ['10.00', '-1', '5.35', '5.00', '0', '1.98', '1.99']  # Compra de dois produtos
    >>> ex_31_conveniencia_manuel.input = lambda k: entradas.pop()
    >>> ex_31_conveniencia_manuel.rodar_programa_de_caixa()
    Lojas Tabajara
    Total     : R$   3.97
    Dinheiro  : R$   5.00
    Troco     : R$   1.03
    -------------------
    Lojas Tabajara
    Total     : R$   5.35
    Dinheiro  : R$  10.00
    Troco     : R$   4.65
    -------------------
    Programa encerrado!

"""


def rodar_programa_de_caixa():
    """Escreva aqui em baixo a sua solução"""
    valor_mercadoria = 0
    dinheiro_pago = 0
    troco = 0
    while True:
        choice = int(input("Digite 2 para continuar a executar o programa, -1 para finalizar a compra, e 0 para fechara a atual e iniciar outra: "))
        if choice == -1:
            break
        elif choice == 0:
            valor_mercadoria = 0
            dinheiro_pago = 0
            troco = 0
        elif choice == 2:
            valor_mercadoria = float(input("Digite o valor da mercadoria comprada"))
            dinheiro_pago = int(input("Dinheiro dado pelo cliente: "))
            troco = dinheiro_pago - valor_mercadoria
    print("Lojas Tabajaras")
    print(f"Total     : R$   {valor_mercadoria}")
    print(f"Dinheiro  : R$   {dinheiro_pago}")
    print(f"Troco     : R$   {troco}")
    print("-------------------")

