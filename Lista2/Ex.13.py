#13. Faça um algoritmo para calcular o valor da conta de energia elétrica de uma casa, considerando a tabela a seguir. A conta deve ser calculada proporcionalmente, ou seja, se o usuário gastou 55 KHW, ele pagará 50 KWH ao preço de R$ 1,00 e 5 ao preço de R$ 1,30. #KWH - Valor
#0 a 50 - R$ 1,00
#51 a 100 - R$ 1,30
#101 a 150 - R$ 1,60
#Acima de 150 - R$ 2.00
#Resposta:

consumo = float(input('Digite quantidade de consumo de KWH:'))
if consumo <= 50:
  print('Sua conta de energia:', consumo * 1.00)
else:
  if consumo >= 51 and consumo <= 100:
    print('Sua conta de energia:', consumo * 1.30)
  else:
    if consumo >= 101 and consumo <= 150:
      print('Sua conta de energia:', consumo * 1.60)
    else:
      print('Sua conta de energia:', consumo * 2.00)