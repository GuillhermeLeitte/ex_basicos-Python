""" Faça um programa que leia um número inteiro, e mostre se é par ou ímpar  """

from os import system
system('clear')
# Estrutura de condição simples
num = int(input('Digite um número: '))

if num % 2 == 0:
    print(f'Esse número {num} é par!')
else:
    print('Esse número {num} é ímpar!!')


""" #Estrutura de condição composta
num = int(input('Digite um número: '))
print(f'Esse número {num} é par!' if num %2 ==0 else 'Esse número {num} é ímpar!!') """
