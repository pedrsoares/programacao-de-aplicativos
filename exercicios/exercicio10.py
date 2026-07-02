import sqlite3

def deletar_escola_antiga():
    id_escola = int(input(" ID da escola a remover: "))
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()


    cursor.execute("DELETE FROM escolas WHERE id = id_escola.db")

    conexao.commit()
    conexao.close()

# Erro: a variável id_escola foi usada de forma errada no comando DELETE.

# CODIGO CORRIGIDO

import sqlite3

def deletar_escola_antiga():
    id_escola = int(input("ID da escola a remover: "))
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM escolas WHERE id = ?", (id_escola,))

    conexao.commit()
    conexao.close()