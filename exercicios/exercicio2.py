import sqlite3

def cadastrar_serie(nome_serie, id_escola):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    try:
        cursor.execute("INSERT INTO series (nome_serie, id_escola) VALUES (?, ?)", (nome_serie, id_escola))
        conexao.commit()
    except sqlite3.IntegrityError:
    print("Erro: Escola inexistente!")
finally:
    conexao.close
