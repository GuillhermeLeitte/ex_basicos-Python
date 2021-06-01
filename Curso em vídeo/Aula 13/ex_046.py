# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

for c in range(10, -1, -1):
    print(c, flush=True)
    sleep(0.8)

print('\U0001F4A3 \U0001F4A5 \U0001F4A5 \U0001F4A3')
sleep(0.5)
print('Feliz Ano Novo!!!')
