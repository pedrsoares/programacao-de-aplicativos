import sqlite3

def verificar_registros():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alunos")

    print("Primeiro print:", cursor.fetchall())
    print("Segundo print:", cursor.fetchall())

    conexao.close()

# Erro: o fetchall() só consegue pegar os dados uma vez. Depois disso, o cursor fica vazio.

# CODIGO CORRIGIDO

import sqlite3

def verificar_registros():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alunos")

    dados = cursor.fetchall()

    print("Primeiro print:", dados)
    print("Segundo print:", dados)

    conexao.close()