ano =int(input("digite um ano "))
if (ano % 4 == 0 and ano % 100 == 1*0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto")
else:
    print(f"O ano {ano} é um ano comum")