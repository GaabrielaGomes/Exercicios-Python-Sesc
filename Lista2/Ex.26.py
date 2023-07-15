#26. Os salários dos empregados de uma empresa sofreram um aumento. Técnicos tiveram um aumento de 50%, gerentes de 30% e os demais de 10%. Faça um programa que calcule o salário reajustado para cada profissão.
#Resposta:

profissao = input("Digite profissão - Técnico, Gerente ou Outros: ")
salarioAtual = float(input("Digite o salário atual: "))

if profissao == "Técnico":
    reajuste = salarioAtual * 1.5
else:
    if profissao == "Gerente":
        reajuste = salarioAtual * 1.3
    else:
        reajuste = salarioAtual * 1.1

print("O novo salário é:", reajuste)
