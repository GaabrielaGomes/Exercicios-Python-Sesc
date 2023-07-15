#30. O Palmeiras deseja aumentar o salário de seus jogadores e comissão técnica para motivá-los na tentiva de subir para a primeira divisão. O ajuste salarial deve obedecer à seguinte tabela:
# Categoria - Salário Atual - Ação
# Equipe técnica -  - Aumento de 15%
# Jogadores - 0 a R$ 9.000,00 - Aumento de 20%
#             9.001,00 a 13.000 - Aumento de 10%
#             13.001 a 18.000 - Aumento de 5%
#             acima de 18.000 - Sem aumento
#Preparar um algoritmo para ler o nome e o salário atual de cada jogador ou técnico e imprimir seu nome, salário atual e salário reajustado.
#Resposta:

nome = input("Digite nome: ")
profissao = input("Digite profissão (Técnico ou Jogador): ")
salario = float(input("Digite o salario atual: "))

if profissao == "Técnico":
  aumento = salario * 0.15
  novoSalario = salario + aumento
  print('Salário do técnico', nome, 'é de R$',novoSalario)
else:
    if profissao == "Jogador":
        if salario <= 9000:
          aumento = salario * 0.20
          novoSalario = salario + aumento
          print('Salário do Jogador', nome, 'é de R$',novoSalario)
        else: 
          if salario >= 9001 and salario <= 13000:
            aumento = salario * 0.10
            novoSalario = salario + aumento
            print('Salário do Jogador', nome, 'é de R$',novoSalario)
          else:
            if salario >= 13001 and salario <= 18000:
              aumento = salario * 0.05
              novoSalario = salario + aumento
              print('Salário do Jogador', nome, 'é de R$',novoSalario)
            else:
              print('Salário do Jogador', nome, 'é de R$',salario, '- Não há aumento')
