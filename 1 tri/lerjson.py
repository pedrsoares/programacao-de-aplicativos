import json

# Abre e lê o arquivo JSON
with open("notas.json", "r", encoding="utf-8") as arquivo:
    dados_notas = json.load(arquivo)

# Obtém apenas os valores (as notas) e faz a soma
soma_notas = sum(dados_notas.values())

# Mostra o resultado na tela
print(f"A soma das notas é: {soma_notas}")