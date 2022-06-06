"""
Exercício 21 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é
divisível somente por ele mesmo e por 1.

    >>> eh_primo(0)
    False
    >>> eh_primo(1)
    False
    >>> eh_primo(2)
    True
    >>> eh_primo(3)
    True
    >>> eh_primo(4)
    False
    >>> eh_primo(5)
    True
    >>> eh_primo(6)
    False
    >>> eh_primo(7)
    True
    >>> eh_primo(8)
    False
    >>> eh_primo(9)
    False
    >>> eh_primo(10)
    False
    >>> eh_primo(11)
    True
    >>> eh_primo(547)
    True
    >>> eh_primo(548)
    False

"""


def eh_primo(n: int) -> bool:
    """Escreva aqui em baixo a sua solução"""
    divi = [2,3,5,7]
    if n == 1 or n == 0:
        print(False)
    else:
        while True:
            if n % divi[0] == 0 or n % divi[1] == 0 or n % divi[2] or n % divi[3]:
                print(False)
                break
            else:
                if n % n == 0 and n % 1 == 0:
                    print(True)
                break

