import sqlite3

conexao = sqlite3.connect('sistema_escola.db')
cursor = conexao.cursor()

def inserir_escola(nome):
    cursor.execute("INSERT INTO escolas(nome) VALUES (?)", (nome,))
    conexao.commit()


# Erro: a conexão deve ser criada dentro da função para evitar problemas em projetos com vários módulos.

# CODIGO CORRIGIDO

def inserir_escola(nome):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO escolas(nome) VALUES (?)", (nome,))
    conexao.commit()
    conexao.close()