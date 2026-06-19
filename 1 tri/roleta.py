senha = input("Digite a senha: ")
tentativa = int(input("Digite o número da tentativa atual: "))
token = input("Você possui Token Especial VIP? (s/n): ")

if senha == "admin123" and (tentativa % 3 == 0 or token == "s"):
    print(f"Tentativa nº {tentativa}: ACESSO CONCEDIDO.")
else:
    print(f"Tentativa nº {tentativa}: ACESSO BLOQUEADO POR PROTOCOLO.")
