#21. Um sistema de equações lineares do tipo: ax+by=c dx+ey=f. pode ser resolvido segundo mostrado: y=af-cd/ae-bd x=ce-bf/ae-bd. Faça um programa que leia os coeficientes a,b,c,d,e,f e calcule e escreva os valores de x e y. 
#Resposta:

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
d = float(input("Digite o valor de d: "))
e = float(input("Digite o valor de e: "))
f = float(input("Digite o valor de f: "))
denominador = a * e - b * d
x = (c * e - b * f) / denominador
y = (a * f - c * d) / denominador
print("O valor de x é:", x)
print("O valor de y é:", y)