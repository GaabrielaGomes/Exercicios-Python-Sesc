# 29. Elaborar um programa que calcule a média ponderada de um aluno da disciplina de Algoritmo. Esta média tem pesos: 4 para a primeira prova e 3 para a segunda prova. Após calculada a média, uma mensagem deve ser apresentada informando a situação do aluno: APROVADO COM MÉDIA ou NECESSITA FAZER SUBSTITUTIVA. Caso o aluno necessite fazer prova substitutiva, o programa deve pedir esta nota e calcular a nova média do aluno. Uma nova mensagem da situação deve informar ALUNO COM MÉDIA ou ALUNO REPROVADO. Obs: A prova substitutiva pode substituir a primeira prova ou a segunda prova, portanto o programa deve verificar quando o aluno fica com maior média, isto é, quando a primeira prova é substituída pela prova substitutiva ou quando a segunda prova é substituída pela prova substitutiva.
#Resposta:

nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
media = (4 * nota1 + 3 * nota2) / 7

if media >= 7.0:
    print("ALUNO APROVADO COM MÉDIA")
else:
    print("ALUNO REPROVADO")
    substitutiva = float(input("\nDigite a nota da prova substitutiva: "))
    if substitutiva > nota1:
        novaMedia = (4 * substitutiva + 3 * nota2) / 7
        print("ALUNO APROVADO COM MÉDIA")
    else:
        novaMedia = (4 * nota1 + 3 * substitutiva) / 7
        print("ALUNO REPROVADO")

