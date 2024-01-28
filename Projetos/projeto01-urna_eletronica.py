'''
EXERCICIO 1:
Urna Eletrônica:
Escreva um algoritmo em Python que considere 3 candidatos em uma votação, a
votação deve ocorrer, enquanto não receber a opção de sair (“S”). Só será
considerado os votos de 1 a 3, os demais podem ser desconsiderados. Após sair
da votação, deve realizar uma verificação para ver qual candidato ganhou a
votação e exibir os votos que cada candidato obteve.

Utilizar as estruturas que vimos em aula.
IF, ELIF, ELSE
MATHC CASE
WHILE OU FOR
'''
from operator import itemgetter
print(f'{"Urna Eletrônica":^41}')
candidatos = {'Lusca': 0,
              'Murilo': 0,
              'Rafaela': 0}
print(f'Votação:')
print('[ 1 ] - Lusca')
print('[ 2 ] - Murilo')
print('[ 3 ] - Rafaela')
print('')
continuar = 'S'
ranking = list()
while True:
    if continuar in 'Ss':
        n = int(input('Escolha seu candidato: '))
        if n >= 1 and n <= 3:
            if n == 1:
                candidatos['Lusca'] += 1
            if n == 2:
                candidatos['Murilo'] += 1
            if n == 3:
                candidatos['Rafaela'] += 1
            continuar = str(input('Continuar votando [S ou N]: '))
        else:
            print(f'Digite um número de 1 á 3')
    else:
        print(f'{"Resultado da votação":-^41}')
        ranking = sorted(candidatos.items(), key=itemgetter(1), reverse=True)
        if candidatos['Lusca'] > candidatos['Murilo'] or candidatos['Lusca'] > candidatos['Rafaela']:
            for n, v in enumerate(ranking):
                print(f'Vencedor em {n + 1}° lugar: {v[0]} com {v[1]} votos')
        elif candidatos['Murilo'] > candidatos['Rafaela'] or candidatos['Murilo'] > candidatos['Lusca']:
            for n, v in enumerate(ranking):
                print(f'Vencedor em {n + 1}° lugar: {v[0]} com {v[1]} votos')
        elif candidatos['Rafaela'] > candidatos['Lusca'] or candidatos['Rafaela'] > candidatos['Murilo']:
            for n, v in enumerate(ranking):
                print(f'Vencedor em {n + 1}° lugar: {v[0]} com {v[1]} votos')
        break
