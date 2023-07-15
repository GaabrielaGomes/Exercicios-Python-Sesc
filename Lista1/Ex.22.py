#22. Faça um programa que leia os valores A,B, C, D, E, F e encontre o valor de X. x=(a+b/c)/d-2*(e/f)+4a
#Resposta:

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))
d = float(input("Digite o valor de D: "))
e = float(input("Digite o valor de E: "))
f = float(input("Digite o valor de F: "))
x = (a + (b / c)) / (d - 2 * (e / f)) 
print("O valor de X é:", x + 4 * a)