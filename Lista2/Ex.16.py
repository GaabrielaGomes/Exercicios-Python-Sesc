#16. Um comerciante está necessitando saber qual é o lucro de cada mercadoria vendida em sua loja. Para isso, está necessitando de um programa que permite informar o valor de custo e de venda de um produto, e imprima uma mensagem considerando a tabela a seguir:
#Lucro - Mensagens
#Inferior a 10% - “Baixo Lucro”
#Entre 10% e 20% - “Lucro Médio”
#Acima de 20% - “Lucro Alto”
#Resposta:

valorCusto = float(input('Digite o valor de custo: '))
valorVenda = float(input('Digite o valor de venda: '))

lucro = ((valorVenda - valorCusto) / valorCusto) * 100

if lucro < 10:
  print('\nBaixo Lucro')
else:
  if lucro > 10 and lucro < 20:
   print('\nLucro Médio')
  else:
    if lucro > 20:
      print('\nLucro Alto')