temperatura_atual = float(input("qual a temperatura atual?"))
if temperatura_atual >= 80:
    print ("PERIGO! Desligando servidor por superaquecimento!")
elif temperatura_atual >= 50:
    print ("Alerta: Ventoinhas ligadas no máximo!")
else:
    print ("Temperatura estável. Sistema operando normalmente")