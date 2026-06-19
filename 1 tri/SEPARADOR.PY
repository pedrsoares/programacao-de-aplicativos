numeros = [1, 5, 8, 12, 15, 22, 7, 9, 30, 4]

par = []
impar = []

for numero in numeros:
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
print (f"IMPAR {impar}")
print (f"PAR {par}")
