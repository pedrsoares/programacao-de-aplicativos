import sqlite3

def vincular_aluno_turma():
    nome = input("Nome do aluno: ")

    try:
        id_turma = int(input("Digite o ID numérico da turma: "))

        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO alunos (nome, id_turma) VALUES (?, ?)", (nome, id_turma))
        conexao.commit()
    except sqlite3.Error:
        print("Erro no banco de dados!")
    finally:
        conexao.close()

# Erro: esta faltando um except para identificar um erro de escrita.


# CODIGO CORRIGIDO

import sqlite3

def vincular_aluno_turma():
    nome = input("Nome do aluno: ")

    try:
        id_turma = int(input("Digite o ID numérico da turma: "))
    except ValueError:
        print("Erro: O ID da turma precisa ser um número inteiro!")
        return
    
    conexao = None
    try:

        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO alunos (nome, id_turma) VALUES (?, ?)", (nome, id_turma))
        conexao.commit()
        print("Aluno vinculado com sucesso!")
    except sqlite3.Error as e:
        print("Erro no banco de dados: {e}")
    finally:
        if conexao:
            conexao.close()

