codigo = int(input("qual o cdigo?"))
autorizaçao = input("voce possui autorizaçao? (s/n)")
 
if codigo == 999 and autorizaçao == "s":
    bateria = int(input("nivel de bateria (0 a 100): "))
    clima = input("clima(ensolarado/chuvoso): ")
    vento= float(input("velocidade do vento"))

    if bateria < 10:
        print ("o pouso deve ser AUTORIZADO IMEDIATAMENTE")

    else: 
        if (clima == "ensolarado" and vento <= 30) or (clima == "chuvoso" and vento <= 10):
            print ("pouso autorizado")
        else:
             print ("POUSO NEGADO: Condições climáticas ou vento inadequados.")

else:
  print("ERRO 01: Drone não identificado. Retornando à base.")



