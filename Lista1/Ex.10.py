#10. Faca um algoritmo que: Peca o valor a prazo do produto, peça a alíquota do desconto e Calcule o preço a vista do produto
#Resposta:

produto = float(input('Digite o valor do produto:'))
aliquota = float(input('Digite o valor da aliquota:'))
porcentagem = produto * (aliquota / 100)
precoProduto =  produto - porcentagem
print('O preço a vista do produto', precoProduto)