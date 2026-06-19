usuarios = ["admin", "convidado", "suporte", "teste"]
usuarios.remove("teste")
del usuarios [0]

print("lista final", usuarios)
print ("usuarios na posiçao 0", usuarios[0])