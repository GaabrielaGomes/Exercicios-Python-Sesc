#27. Suponha que um caixa disponha apenas notas de 100, 10 e 1 Real. Considerando que alguém está pagando uma compra, faça um programa para determinar o número mínimo de notas que o caixa deve fornecer como troco. Imprima também o valor da compra, o valor do troco e a quantidade de cada tipo de nota a ser fornecido como troco. Suponha que o sistema monetário não utilize centavos. 
#Resposta:

valorCompra = int(input("Digite o valor da compra: "))
Pagamento = int(input("Digite o valor pago: "))
troco = Pagamento - valorCompra
nota100 = troco // 100
troco = troco % 100
nota10 = troco // 10
troco = troco % 10
nota1 = troco

print("\nValor da compra:", valorCompra)
print("Valor do troco:", Pagamento - valorCompra)
print("Notas de R$ 100:", nota100)
print("Notas de R$ 10:", nota10)
print("Notas de R$ 1:", nota1)
