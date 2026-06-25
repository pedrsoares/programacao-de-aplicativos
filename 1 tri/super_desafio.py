livros_disponiveis = ["Python Pro", "Banco de Dados", "Redes", "IA", "Hardware"]
livros_emprestados = []
livro = input("digite o livro que voce quer")

if livro in livros_disponiveis:
    livros_disponiveis.remove(livro)
    livros_emprestados.append(livro)
    print ("emprestimo realizado co  sucesso!")
else:
    print ("Desculpe, este livro não está no acervo")



livro_emprestado = input("digite o nome do livro para devoluçao")
if livro_emprestado in livros_emprestados:
    livros_emprestados.remove(livro_emprestado)
    livros_disponiveis.append(livro_emprestado)
    print("livro devolvido com sucesso")
else:
    print("este livro nao e emprestado")

del livros_disponiveis[0:2]
print (f"estado final da duas listas: {livros_disponiveis} e lista do empretimo: {livro_emprestado}")
