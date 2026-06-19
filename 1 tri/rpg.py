
heroi_atq = float(input("quantos pontos de ataque voce vai causar?"))
vilao_def = float(input("quantos pontos de defesa o vilao tem?"))
dano = heroi_atq - vilao_def



if dano >= 0:
    print ( "ataque critico voce causou" ,  dano)
elif dano <= 0:
    print ("O vilão bloqueou o ataque!" , dano ) 
