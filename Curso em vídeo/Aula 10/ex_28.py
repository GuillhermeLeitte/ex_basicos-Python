# Escreva um programa que faça o cumputador pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário ganhou ou perdeu.

from random import randint
from os import system
comp = randint(0, 5)

system('clear')

print('Eu pensei em um número , será que você consegue descobrir qual foi?')
user = int(input('Escolha um número entre 0 e 5: '))
c = 1
while True:
    if user != comp:
        print(f'Você errou, tente novamente...\n')
        c += 1
        print(f'Dica: não é o número {user}')
        user = int(input('Escolha um número entre 0 e 5: '))
    else:
        system('clear')
        print('Você acertou!!!')

        break
print(f'Você precisou de {c} tentativas para acertar')
print('Fim do programa...')


# Estrutura de condição simples
""" if user == comp:
    print('VOCÊ DESCOBRIU PARABÉNS!!') 
else:
    print('VOCÊ ERROU, tente novamente...')
print('Fim do programa')
 """
# Estrutura de condição composta
#print('VOCÊ DESCOBRIU PARABÉNS!!!'if user == comp else 'VOCÊ ERROU, tente novamente...')
