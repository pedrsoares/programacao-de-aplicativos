usuario = input("qual o nopme de usuario")
senha = int(input("qual a senha?"))

if (usuario == "admin" or usuario == "root") and senha == 1234:
    print ("aceso liberado")
else:
    print ("acesso negado")
