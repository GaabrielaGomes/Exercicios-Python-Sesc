#28. Calcule a média aritmética de três valores A, B e C, escrevendo o valor e a mensagem apropriada:
# Média > 9 ► Aluno Excelente
# Média <= 9 e média > 8, ► Bom Aluno
# Média <= 8 e média > 7, ► Aluno Regular
# Média <= 7 e média > 6, ► Aluno Aprovado
# Média <= 6 e média > 5, ► Aluno de Exame
# Caso contrário, mostre a mensagem reprovado
#Resposta:

notaA = float(input("Digite a nota A: "))
notaB = float(input("Digite a nota B: "))
notaC = float(input("Digite oa nota C: "))
media = (notaA + notaB + notaC) / 3

if media > 9:
    print('Média:',media,'Aluno Excelente')
elif media <= 9 and media > 8:
    print('Média:',media,'Bom Aluno')
elif media <= 8 and media > 7:
    print('Média:',media,'Aluno Regular')
elif media <= 7 and media > 6:
    print('Média:',media,'Aluno Aprovado')
elif media <= 6 and media > 5:
    print('Média:',media,'Aluno de Exame')
else:
    print('Média:',media,'Reprovado')

