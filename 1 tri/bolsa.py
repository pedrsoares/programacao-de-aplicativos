med = float(input("qual a sua media?"))
renda = float(input("qual a sua renda?"))
esc = input("voce veio de escola publica? (s/n)")
 
if med >= 8.0 and (renda <2.000 or esc == "s"):
    print ("voce ganhou a bolsa")
else:
    print (" voce nao ganhou a bolsa")
