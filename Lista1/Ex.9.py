#9. Desenvolva um algoritmo que: Peca o valor do produto, peca a valor da aliquota e calcule o valor em reais da porcentagem informada.
#Resposta:

produto = float(input('Digite o valor do produto:'))
aliquota = float(input('Digite o valor da aliquota:'))
porcentagem = produto * (aliquota / 100)
print('valor em reais da porcentagem', porcentagem)