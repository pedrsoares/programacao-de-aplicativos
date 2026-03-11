codigo = int(input("qual o codigo do produto"))
peso = float(input(" qual o peso do produto? (kg)"))


if peso < 5 and codigo % 10 == 0:
    status = "entrega expressa"
    print (f"pacote {codigo}: {status}")

elif peso > 50:
    status = "entrega pesada"
    print (f"pacote {codigo}: {status}")

