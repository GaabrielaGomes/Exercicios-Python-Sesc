#4. Uma empresa de modelo está contratando garotas para iniciar um trabalho de divulgação de produtos de beleza. Para isso, está selecionando garotas que tenham o seguinte perfil:
#a. Idade superior a 18 anos
#b. Cabelos Loiros
#c. Altura superior a 1,75 m
#d. Peso inferior a 60 kg
#e. Seios: 85 a 87 cm
#f. Cintura: 60 cm
#g. Olhos verdes
#h. Quadril = 60 cm
#Você foi escalado por sua empresa para elaborar um algoritmo que permite entrar com os valores referentes às características acima e, informar se a garota foi selecionada ou não.
#Resposta:

idade = int(input('Digite sua idade: '))
cabelo = input('Digite a cor de cabelo: ')
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
seios = float(input('Digite a medida dos seios: '))
cintura = float(input('Digite medida da cintura: '))
olhos = input('Digite a cor dos olhos: ')
quadril = float(input('Digite medida do quadril: '))

if idade > 18 and cabelo == 'Loiros' or 'loiros' and altura > 1.75 and peso < 60 and seios >= 85 or seios <= 87 and cintura == 60 and olhos == 'Verdes' or 'verdes' and quadril == 60:
  print('\nVocê foi selecionada')
else:
     print('\nVocê não foi selecionada')