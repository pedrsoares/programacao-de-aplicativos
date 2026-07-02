import sqlite3

def cadastrar_turma(nome, id_serie, id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    cursor.execute("INSERT INTO turmas (nome_turma, id_serie, id_professor) VALUES (?, ?, ?)", (nome, id_serie, id_prof))
    conexao.commit()
    conexao.close()

# Erro: A linha conexao.close() não é executada. O erro interrompe o programa antes de chegar nela, e a conexão com o banco de dados continua aberta na memória.

# CODIGO CORRIGIDO

import sqlite3

def cadastrar_turma(nome, id_serie, id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    try:
        cursor.execute("INSERT INTO turmas (nome_turma, id_serie, id_professor) VALUES (?, ?, ?)", (nome, id_serie, id_prof))
        conexao.commit()
    except sqlite3.IntegrityError:
        print("Erro: O id_prof ou id_serie fornecido não existe!")
    finally:
        conexao.close()