#16. Você foi encarregado de desenvolver o modulo de cálculo da folha de pagamento de uma empresa. O funcionamento do programa deve ser o seguinte:Peça o nome do empregado, Peça o salário bruto, Peça o valor do Imposto de Renda em reais que será descontado, Peça o valor da previdencia (INSS) em reais que será descontado e Calcule o valor do salário liquido do empregado. Informe o salário liquido com a seguinte frase:Fulano, seu salário liquido é: ......
#Resposta:

nome = (input('Digite seu nome: '))
salarioBruto = float(input('Digite seu salário bruto: '))
imposto = float(input('Digite valor do imposto em reais: '))
inss = float(input('Digite valor da previdencia (INSS) em reais: '))
print(nome, 'seu salário liquido é:', salarioBruto - (imposto+inss))