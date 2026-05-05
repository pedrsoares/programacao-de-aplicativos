def gerar_relatorio_saude(nome, peso, altur, idade):
    imc = peso / (altura ** 2)

    if imc < 18.5:
        categoria = "baixo peso"
    elif 18.5 <= imc <= 24.9:
        categoria = "normal"
    elif 25 <= 29.9:
        categoria = "sobrepeso"
    else:
        categoria = "obesidade"

    
    return f"relatorio: {nome} ({idade} anos) possui IMC de {imc} - categoria: {categoria}"
n = input("nome:")
p = float(input("peso (kg):"))
a = float(input("altura (m): "))
i = int(input("idade: "))

print(gerar_relatorio_saude(n, p, a, i))