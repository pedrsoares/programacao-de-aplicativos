curso = input ("voce concluio o curso (s/n)")
if curso == "n":
    print ("Acesso Negado: Faça o treinamento primeiro.")
else:
    intrutor = input("O Instrutor está presente na sala? (s/n)")
    if intrutor == "s":
        print ("Acesso Liberado: Operação iniciada")
    else:
        print ("Aguarde o instrutor para ligar a máquina")
        
