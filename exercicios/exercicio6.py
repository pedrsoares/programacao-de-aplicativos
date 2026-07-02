import sqlite3

def buscar_professor(id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()


    cursor.execute("SELECT nome FROM professores WHERE id = ?", (id_prof)) # Erro: falta da vírgula depois de id_prof para indicar que é uma tupla
    resultado = cursor.fetchone()
    print(resultado)
    conexao.close()


# CODIGO CORRIGIDO 

import sqlite3

def buscar_professor(id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()


    cursor.execute("SELECT nome FROM professores WHERE id = ?", (id_prof,)) 
    resultado = cursor.fetchone()
    print(resultado)
    conexao.close()