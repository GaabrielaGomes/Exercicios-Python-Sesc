#18. Dado três números digitados pelo usuário, e todos diferentes, imprima o maior número.
#Resposta:

numeroA = float(input('Digite número A: '))
numeroB = float(input('Digite número B: '))
numeroC = float(input('Digite número C: '))

if numeroA > numeroB and numeroC:
 print('Numero A é maior')
else:
  if numeroB > numeroC and numeroA:
    print('Numero B é maior')
  else:
    if numeroC > numeroA and numeroB:
      print('Numero C é maior')
    else:
      print('Eles são iguais')