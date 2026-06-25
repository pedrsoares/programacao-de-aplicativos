pendentes = ["relatorio.pdf", "foto.png" , "planilha.xlsx" ]
conclido = []
print("estado inicial:")
print(f"pendentes: {pendentes}")
print(f"concluidos: {concluidos}")
print()

arquivo = pendentes.pop(0)
concluidos.append(arquivo)

print("apos transferencia:")
print(f"pendentes:{pendentes}")
print(f"concluidos{concluidos}")