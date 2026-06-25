import sqlite3

conexao = sqlite3.connect('escola_demosntracao.db')
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT,
        turma TEXT,
        idade INTEGER,
        cpf TEXT UNIQUE NOT NULL
    )
''')

nome_aluno = input("Nome: ")
telefone_aluno = input("Telefone: ")
turma_aluno = input("Turma: ")
idade_aluno = int(input("Idade: "))
cpf_aluno = input("CPF: ")

comando_inserir = f'''
    INSERT INTO alunos (nome, telefone, turma, idade, cpf)
    VALUES ('{nome_aluno}', '{telefone_aluno}', '{turma_aluno}', {idade_aluno}, '{cpf_aluno}')
'''

cursor.execute(comando_inserir)

print("Aluno cadastrado com sucesso!")

cursor.execute("SELECT * FROM alunos")
print("Lista: ")

todos_alunos = cursor.fetchall()
 if not todos_alunos:
    print("Nenhum aluno cadastrado!")
else:
    for aluno in todos_alunos:
        print(f"ID:{aluno[0]} | Nome: {aluno[1]} | Telefone: {aluno[2]} | Turma: {aluno[3]} | Idade: {aluno[4]} | CPF: {aluno[5]}")
        
conexao.commit()
conexao.close()