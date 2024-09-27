"""
Exercício 45 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno
a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a
nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro
aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:

Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma com uma casa decimal.

Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A

    >>> corrigir(('Renzo','A','B','C','D','E','E','D','C','B','A' ))
    Aluno                 Nota
    Renzo                 10
    ---------------------------
    Média geral: 10.0
    Maior nota: 10
    Menor nota: 10
    Total de Alunos: 1
    >>> corrigir(
    ... ('Renzo','A','B','C','D','E','E','D','C','B','A' ),
    ... ('Fulano','A','B','C','D','E','E','D','C','B','B' ),
    ... )
    Aluno                 Nota
    Renzo                 10
    Fulano                 9
    ---------------------------
    Média geral: 9.5
    Maior nota: 10
    Menor nota: 9
    Total de Alunos: 2
"""


def corrigir(*provas):
    """Escreva aqui em baixo a sua solução"""
    gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
    a, *b = provas[0]
    acertos_aluno_01 = 0
    erros_aluno_01 = 0
    acertos_aluno_02 = 0
    erros_aluno_02 = 0
    maior_nota = 0
    menor_nota = 0
    media = 0
    for cont in range(0, len(b)):
        if b[cont] == gabarito[cont]:
            acertos_aluno_01 += 1
        else:
            erros_aluno_01 += 1
    media = acertos_aluno_01 / len(provas)
    if len(provas) == 1:
        print("Aluno                 Nota")
        print(f"{a}                 {acertos_aluno_01}")
        print("---------------------------")
        print(f"Média geral: {media:.1f}")
        print(f"Maior nota: {acertos_aluno_01}")
        print(f"Menor nota: {acertos_aluno_01}")
        print(f"Total de Alunos: {len(provas)}")

    if len(provas) >= 2:
        c, *d = provas[1]
        for cont in range(0, len(d)):
            if d[cont] == gabarito[cont]:
                acertos_aluno_02 += 1
            else:
                erros_aluno_02 += 1
        if acertos_aluno_01 > acertos_aluno_02:
            maior_nota = acertos_aluno_01
            menor_nota = acertos_aluno_02
        else:
            maior_nota = acertos_aluno_02
            menor_nota = acertos_aluno_01
        media = (acertos_aluno_01 + acertos_aluno_02) / len(provas)
        print("Aluno                 Nota")
        print(f"{a}                 {acertos_aluno_01}")
        print(f"{c}                 {acertos_aluno_02}")
        print("---------------------------")
        print(f"Média geral: {media:.1f}")
        print(f"Maior nota: {maior_nota}")
        print(f"Menor nota: {menor_nota}")
        print(f"Total de Alunos: {len(provas)}")


