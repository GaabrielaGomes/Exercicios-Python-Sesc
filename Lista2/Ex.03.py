#3. Repita o exercício anterior sabendo que os números são diferentes, qual é o maior e o menor dos números.
#Resposta:

numeroA = int(input('Digite o número de A: '))
numeroB = int(input('Digite o número de B: '))

if numeroA != numeroB:
  if numeroA > numeroB:
    print('Número A é maior') 
  else:
    print('Número B é maior')
else:
  print('Os números são iguais')