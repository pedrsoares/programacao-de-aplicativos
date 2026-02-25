altura =float(input("qual a sua altura?"))
nome = input("qual eo seu nome?")

if altura <1.50:
    print ( "Desculpe, você não tem a altura mínima" , nome)
elif altura >=1.50:
    print ("Acesso liberado! Divirta-se na queda livre" , nome)