#7. Leia um número para verificar se ele é maior do que 20. Caso afirmativo imprima a metade desse número. Caso contrário imprima o seu quadrado
#Resposta: 

numero = float(input('Digite o valor de A: '))

if numero >= 20:
  print('A metade do número:', numero/2) 
else:
  print('O quadrado do número:', numero**2)