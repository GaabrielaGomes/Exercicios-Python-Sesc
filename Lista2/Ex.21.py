#21. Faça um algoritmo para determinar o maior e o menor de quatro números lidos.
#Resposta:

numeroA = float(input('Digite número A: '))
numeroB = float(input('Digite número B: '))
numeroC = float(input('Digite número C: '))
numeroD = float(input('Digite número D: '))

if numeroA < numeroB and numeroA < numeroC and numeroA < numeroD:
 print('\nNumero A é menor')
else:
  if numeroB < numeroC and numeroB < numeroA and numeroB < numeroD:
    print('\nNumero B é menor')
  else:
    if numeroC < numeroA and numeroC < numeroB and numeroC < numeroD:
      print('\nNumero C é menor')
    else:
      if numeroD < numeroA and numeroD < numeroB and numeroD < numeroC:
       print('\nNumero D é menor')
      else:
        print('\nEles são iguais')

if numeroA > numeroB and numeroA > numeroC and numeroA > numeroD:
 print('Numero A é maior')
else:
  if numeroB > numeroC and numeroB > numeroA and numeroB > numeroD:
    print('Numero B é maior')
  else:
    if numeroC > numeroA and numeroC > numeroB and numeroC > numeroD:
      print('Numero C é maior')
    else:
      if numeroD > numeroA and numeroD > numeroB and numeroD > numeroC:
       print('Numero D é maior')
      else:
        print('Eles são iguais')