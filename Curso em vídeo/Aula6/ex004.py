# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

algo = input('Digite algo: ')

print('o tipo primitivo desse valor é', type(algo))

print('Só tem espaços?',algo.isspace())

print('É um número?',algo.isnumeric())

print('É alfabético?',algo.isalpha())

print('É alfanumérico?',algo.isalnum())

print('Está todo em maiúscula?',algo.isupper())

print('Está todo em minúscula?',algo.islower())

print('Está Capitalizada?',algo.istitle())
