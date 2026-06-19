idade =int(input("qual a sua iadade?"))
ingresso =input("voce tem o ingresso? (s/n): ")
lista =input ("voce esta na lista? (s/n)")

if (idade > 18 and ingresso == "s") or lista == "s":
    print ('acesso permitido')
else:
    print ('acesso negativo')
    


