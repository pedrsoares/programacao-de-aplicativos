valor = float(input("qual o valor da compra?"))
prime = input("voce e assinante prime? (s/n)")

if valor >= 500.00 or prime == "s" and valor < 100:
    frete = 0
else:
    frete = 50
    print ("frete de 50 reais adicionado")
total = valor + frete

print ("valor da compra foi de" , total)

    

