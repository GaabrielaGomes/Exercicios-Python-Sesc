#25. Escreva um programa para calcular o reajuste salarial dos empregados de uma empresa, de acordo com os seguintes critérios:
#a. Os funcionários com salário inferior a 1.000,00 devem ter um reajuste de 55%;
#b. Funcionários com salário de 1.000,00 (inclusive) a 2.500,00 (inclusive) devem ter um reajuste de 33%;
#c. Os funcionários com salário superior a 2.500,00 devem ter um reajuste de 20%;
#Resposta:

salario = float(input("Digite o valor do salário do funcionário: "))

if salario < 1000:
    reajuste = salario * 0.55
elif salario >= 1000 and salario <= 2500:
    reajuste = salario * 0.33
else:
    reajuste = salario * 0.20

total = salario + reajuste

print("O novo salário é:", total)
