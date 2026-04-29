def eh_par(numero):
    return numero % 2 == 0

numero = int(input("Digite um número: "))

if eh_par(numero):
    print("Este número é par")
else:
    print("Este número é ímpar")
