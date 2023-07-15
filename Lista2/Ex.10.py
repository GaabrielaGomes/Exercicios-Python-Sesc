#10. Faça um algoritmo para calcular a conta de energia elétrica de uma casa. O valor de cada KWH é 1.5. Quando a casa é de uma aposentada, a conta tem um desconto de 15%.
#Resposta: 

energia = float(input('Digite quantidade de KWH: '))
aposentada = bool(input('Voce é aposentado(a)?: '))
kwh = energia * 1.5

if aposentada != True:
  print('O valor da energia com 15% de desconto:', kwh - (kwh*0.15))
else:
   print('O valor da energia sem desconto:', kwh)