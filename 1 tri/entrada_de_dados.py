carrinho = []
item = ""
while item != "fim":
    item = input("Produto: ")
    if item != "fim":
        carrinho.append(item)
for produto in carrinho:
    print(produto)