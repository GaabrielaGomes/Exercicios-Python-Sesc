#15. Desenvolva um algoritmo para calcular quantos reais serão necessários para encher o tanque de um veiculo para se realizar uma viagem. O usuário deverá informar o tipo de combustível do veículo, o número total de km a ser percorrido e o consumo médio do veículo. A tabela de preços dos combustíveis utilizada no cálculo é apresentada abaixo:
#Combustível - Preço
#Gasolina - 22.25
#Álcool - 11.5
#Diesel - 11.65
#Resposta:

combustivel = input('Digite qual combustível: ')
km = float(input('Digite quantos KM serão percorridos: '))
consumo = float(input('Digite o consumo médio do veículo: '))
litros = km / consumo
if combustivel == 'Álcool' or combustivel == 'alcool':
  print('\nVocê gastará R$', litros * 11.5)
else:
 if combustivel == 'Gasolina' or combustivel == 'gasolina':
  print('\nVocê gastará R$', litros * 22.25)
 else:
  if combustivel == 'Diesel':
   print('\nVocê gastará R$', litros * 11.65)
  else:
   print('\nCombustível não identificado')
