#12. Faça um algoritmo para calcular o valor da conta de água, considerando a seguinte tabela de gastos: 0 – 10 M3 = R$ 1,20, 11 – 20M3 = R$ 1,50 e acima de 20M3 = R$ 2,00
#Resposta:

consumo = float(input("Digite o consumo de água em metros cúbicos: "))

if consumo <= 10:
    valor = consumo * 1.20
else:
    if consumo <= 20:
        valor = consumo * 1.50
    else:
        valor = consumo * 2.00

print("O valor da conta de água é: R$", valor)