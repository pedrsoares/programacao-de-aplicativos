autorizados = ["alice" , "bob" , "carlos"]

nome =input("digite o nome do pesquisador:")

if nome in autorizados:
    indice = autorizados.index(nome)
    print(f"aceso permitido! o pesquisador {nome} esta na posiçao {indice}.")

    confirmaçao = input(f"deseja remover {nome} da lista? (sim/nao):")
    if confirmaçao == "sim":
        autorizados.remove(nome)
        print(f"pesquisador removido lista autualizada: {autorizados}")
else:
    print:(f"acesso negado, o pesquisador {nome} nao foi encontrado")

    cadastro = input(f"deseja cadastrar {nome} como novo pesquisador? (sim/nao):")
    if cadastro == "sim":
        autorizados.append(nome)
        print(f"pesquisador cadastrado, lista autualizado {autorizados}")


