import sqlite3

conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS professor (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT,
        turma TEXT,
        idade INTEGER,
        cpf TEXT UNIQUE NOT NULL,
        materia TEXT,
        salario TEXT NOT NULL,
        escola TEXT NOT NULL
    )
''')

nome_professor = input("Nome: ")
telefone_professor = input("Telefone: ")
turma_professor = input("Turma: ")
idade_professor = int(input("Idade: "))
cpf_professor = input("CPF: ")
materia_professor = input("Materia: ")
salario_professor = input("Salario: ")
escola_professor = input("Escola: ")


comando_inserir = f'''
    INSERT INTO professor (nome, telefone, turma, idade, cpf, materia, salario, school)
    VALUES ('{nome_professor}', '{telefone_professor}', '{turma_professor}', '{idade_professor}', '{cpf_professor}', '{materia_professor}', '{salario_professor}', '{escola_professor}')
'''

cursor.execute(comando_inserir)
conexao.commit() 

print("Professor cadastrado com sucesso!")

cursor.execute("SELECT * FROM professor")
print("Lista: ")

todos_professor = cursor.fetchall()


if not todos_professor:
    print("Nenhum professor cadastrado!")
else:
    for professor in todos_professor:
        print(f"ID:{professor[0]} | Nome: {professor[1]} | Telefone: {professor[2]} | Turma: {professor[3]} | Idade: {professor[4]} | CPF: {professor[5]} | Materia: {professor[6]} | Salario: {professor[7]} | Escola: {professor[8]}")
        
conexao.close()