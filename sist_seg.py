nome_usuario =input('qual eo nome de usuario?')
cod =int(input("qual eo codigo?"))
if nome_usuario == "admin" and cod == 999:
    print ("Acesso ao servidor liberado. Sistema online.")
else:
    print ("Falha na autenticação. Alerta de segurança ligado!")
