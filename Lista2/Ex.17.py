#17. O comerciante, ainda não satisfeito, solicitou a empresa de informática responsável pelos programas em sua loja, um programa que permite saber o lucro médio obtido quando acontece a compra por um cliente. Para isso, será necessário saber quantos produtos de cada tipo foi comprado pelo cliente, e fazer a média dos lucros em porcentagem.
#Resposta:

valorCustoProdutoA = float(input('Digite o valor do custo produto A: '))
valorVendaProdutoA = float(input('Digite o valor da venda produto A: '))
valorCustoProdutoB = float(input('Digite o valor do custo produto B: '))
valorVendaProdutoB = float(input('Digite o valor da venda produto B: '))

lucroA = ((valorVendaProdutoA - valorCustoProdutoA) / valorCustoProdutoA) * 100
lucroB = ((valorVendaProdutoB - valorCustoProdutoB) / valorCustoProdutoB) * 100

print('\nLucro médio:', (lucroA + lucroB)/2)