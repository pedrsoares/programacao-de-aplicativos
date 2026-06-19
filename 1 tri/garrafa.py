vagas = ["Ocupado", "Livre", "Ocupado", "Livre"]

indice = int(input("Digite o número da vaga (0 a 3): "))

if 0 <= indice <= 3:
    if indice % 2 == 0 and vagas[indice] == "Livre":
        print(f"Vaga {indice} autorizada para estacionar.")
    else:
        print(f"Vaga {indice} indisponível ou fora das regras.")
else:
    print("Índice inválido.")