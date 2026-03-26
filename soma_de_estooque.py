
precos = [19.90, 45.00, 12.50, 89.99, 5.25]

total_estoque = 0


for preco in precos:
    total_estoque += preco


print(f"O valor total do estoque é: R$ {total_estoque:.2f}")
