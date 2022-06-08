"""
Exercício 22 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é
divisível.
    >>> eh_primo(0)
    False
    >>> eh_primo(1)
    False
    >>> eh_primo(2)
    True
    >>> eh_primo(3)
    True
    >>> eh_primo(4)
    É divisível por 2
    False
    >>> eh_primo(5)
    True
    >>> eh_primo(6)
    É divisível por 2
    É divisível por 3
    False
    >>> eh_primo(7)
    True
    >>> eh_primo(8)
    É divisível por 2
    É divisível por 4
    False
    >>> eh_primo(9)
    É divisível por 3
    False
    >>> eh_primo(10)
    É divisível por 2
    É divisível por 5
    False
    >>> eh_primo(11)
    True
    >>> eh_primo(12)
    É divisível por 2
    É divisível por 3
    É divisível por 4
    É divisível por 6
    False
    >>> eh_primo(547)
    True

"""


def eh_primo(n: int) -> bool:
    """Escreva aqui em baixo a sua solução"""
    import math
    possiveis_divisores = math.ceil(n / 2)
    denominador = 1
    divisores = 0
    resto_par = [2,4]
    cont = 0
    if n == 0 or n == 1:
        print("False")

    else:
        while denominador <= possiveis_divisores:
            if n % resto_par[0] == 0 or n % resto_par[1] == 0:
                print(f"É divisivel por {resto_par[cont]}")
                cont += 1
            if n % denominador == 0:
                divisores += 1
            denominador += 1
        if divisores > 1:
            print("False")
        else:
            print("True")