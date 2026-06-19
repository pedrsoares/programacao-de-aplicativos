import sqlite3

conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()

def criar():

    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS professores (
                        id  INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome completo TEXT NOT NULL,
                        telefone TEXT,
                        materia TEXT,
                        idade INTERGER,
                        cpf TEXT UNIQUE NOT NULL,
                        salario REAL,
                        escola TEXT
                    )
                ''')

    nome_completo = input("Digite o nome do professor: ")
    telefone = input("Digite o telefone do professor: ")
    materia = input("Digite a materia do professor: ")
    idade = int(input("Digite a idade do professor: "))
    cpf = input("Digite o cpf do professor: ")
    salario = input("Digite o salario do professor: ")
    escola = input("Digite a escola do professor: ")

    comando_inserir = f'''
            INSERT INTO  professores (nome, telefone, materia, idade, cpf, salario, escola)
            VALUES ('{nome_completo}', '{telefone}', '{materia}', {idade}, '{cpf}', {salario}, '{escola}')
            '''

    cursor.execute(comando_inserir)

    conexao.commit()

    print("cadastro realizado!")

    


def listar():

    cursor.execute("SELECT * FROM professores")

    professores = cursor.fetchall()

    print("=== Lista de Professor ===")

    for professor in professores:
        print(f"ID: {professor[0]}")
        print(f"Nome: {professor[1]}")
        print(f"Materia: {professor[2]}")
     
        print(f"Idade: {professor[3]}")
        print(f"CPF: {professor[4]}")
        print(f"Salario: {professor[5]}")
        print(f"Escola: {professor[6]}")
        print("-" * 30)

        
def alterar():

    id_professor = int(input("Qual é o teu ID: "))

    cursor.execute(f'''SELECT * FROM professores WHERE id = {id_professor}''')
    professor = cursor.fetchone()

    if not id_professor:
        print("Não encontrado!")
    else:
        print(f"Nome atual {professor[0]} ")
        print(f"Materia atual {professor [1]} ")
        print(f"Idade atual {professor[2]} ")
        print(f"CPF atual {professor [3]} ")
        print(f"Salario atual {professor [4]} ")
        print(f"Escola atual {professor [5]} ")

        nome_atualizado = input("Atualize teu nome: ")
        telefone_atualizado = input("Atualize teu telefone: ")
        materia_atualizada = input("Atualize tua materia: ")
        idade_atualizada = input("Atualize tua idade: ")
        cpf_atualizado = input("Atualize teu CPF: ")
        salario_atualizado = input("Atualize teu salario: ")
        escola_atualizada = input("Atualize tua escola: ")


        cursor.execute(f'''
                        UPDATE professores
                        SET nome ='{nome_atualizado}', telefone ='{telefone_atualizado}', materia ='{materia_atualizada}', idade ={idade_atualizada}, cpf ='{cpf_atualizado}' , salario ={salario_atualizado}, escola ='{escola_atualizada}'
                    WHERE id ={id_professor}
                        ''')
        conexao.commit()
        print(" Dados alterados ")

    
def deletar():
    id_professor = int(input(" Qual ID deseja deletar: " ))

    cursor.execute(f'''SELECT * FROM professores WHERE id = {id_professor}''')
    professor = cursor.fetchone()

    if not professor:s
        print ("Professor não encontrado ")
    else:
        cursor.execute(f'''DELETE FROM professores WHERE id = {id_professor}''')
        conexao.commit()
        print("Professor deletado")

        
def menu():
    opcao = 0
    while opcao != 5:
        print("\n----CADASTRANDO PROFESSORES---")
        print("\n1 - criar ")
        print("\n2 - listar ")
        print("\n3 - alterar ")
        print("\n4 - deletar ")
        print("\n5 - Sair ")

        opcao = int(input("Digite uma opcao: "))

        if opcao == 1: criar()
        elif opcao == 2: listar()
        elif opcao == 3: alterar()
        elif opcao == 4: deletar()
        elif opcao == 5:
            conexao.close()
            print("PROGRAMA ENCERRADO")
            

menu()


