import sqlite3

conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()

cursor.execute(''' DROP TABLE professores''')

conexao.commit()
conexao.close()