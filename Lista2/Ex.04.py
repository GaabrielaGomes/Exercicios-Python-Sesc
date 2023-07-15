#4. Leia um número e, se ele for positivo, imprima seu inverso; caso contrário imprima seu quadrado Inverso. Inverso: 1/número. 
#Resposta:

numero = float(input('Digite um número: '))
inverso = 1/numero

if numero > 0:
    print('O inverso:', inverso) 
else:
  print('O quadrado inverso:', inverso*inverso)