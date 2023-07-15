#Faça um algoritmo que leia os valores A, B, C e diga se a soma de A + B é menor que C
#Resposta:

valorA = int(input('Digite o valor de A: '))
valorB = int(input('Digite o valor de B: '))
valorC = int(input('Digite o valor de C: '))
soma = valorA + valorB

if soma > valorC:
  print('A soma é maior:') 
else:
 if soma==valorC:
  print('A soma é igual')
 else:
  print('A soma é menor')