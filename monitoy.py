temp = float(input("qual a temperatura atual?"))
if temp < 30:
    print ("Clima estáve")
    if temp >= 30:
        print ("Alerta de Calor!")
        umidade = float(input("qual a umidade?"))
        if umidade < 40:
            print ("Ação: Ligar Irrigação!")
        else:
            print ("Ação: Ligar apenas ventiladores")
            