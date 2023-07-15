#5. Faça um algoritmo para imprimir a média e informar se o aluno foi aprovado ou reprovado e, qual a média obtida.
#Resposta:

notaA = float(input('Digite a nota A: '))
notaB = float(input('Digite a nota B: '))
media = (notaA + notaB)/2

print('Sua média:', media)

if media >= 6:
  print('Você foi aprovado')
else:
  print('Você foi reprovado')