#8. Leia um número e imprima se ele é positivo, negativo ou nulo.
#Resposta:

numero = int(input('Digite um número: '))

if numero > 0:
  print('O número é positivo') 
else:
 if numero < 0:
  print('O número é negativo')
 else:
  print('O numero é nulo')