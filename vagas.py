vagas = ["Ocupado", "Livre", "Ocupado", "Livre"]
digite = int(input("digite o numero de a 0 a 3 "))

if 0 <= digite <= 3:
    if digite % 2 == 0 and vagas[digite] == "Livre":
        print(f"Vaga {digite} autorizada para estacionar.")
    else:
        print(f"Vaga {digite} indisponível ou fora das regras.")
else:
    print("Índice inválido.")