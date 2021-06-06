""" 
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada km acima do limite.
 """

from os import system

system('clear')

vel_carro = float(input('Qual foi a velocidade do carro? '))
limite = 80
if vel_carro > 80:

    print(
        f'Você ultrapassou o limite de {limite}km/h de velocidade, será multado!')

    multa = (vel_carro - limite) * 7

    print(
        f'A multa será de R$ 7,00 por cada km ultrapassado...\n A multa é de R${multa:.2f}')
