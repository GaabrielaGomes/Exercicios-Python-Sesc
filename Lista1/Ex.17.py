#17. Você foi contratado por uma empresa de construção para fazer um programa que calcule o salário liquido dos operários no fim de cada mês, sabe-se que cada operário recebe R$ 3,00 por cada hora trabalhada, e que se desconta 8% do salário bruto para INSS.
#Resposta:

horasTrabalhadas = float(input('Digite total de horas trabalhadas:'))
print('Salário liquido:', horasTrabalhadas*3.0-0.08)