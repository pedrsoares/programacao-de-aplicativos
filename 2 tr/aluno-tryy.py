import sqlite3

def conectar():
    try:
        conexao = sqlite3.connect('escola.demonstracao.db')
        cursor = conexao.cursor()
        cursor.execute('PRAGMA foreign_keys = ON;')
    
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS professores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
        ''')
    
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT,
            turma TEXT,
            idade INTEGER,
            cpf TEXT UNIQUE NOT NULL,
            professor_id INTEGER,
            endereco TEXT,
            cidade TEXT,
            estado TEXT,
            FOREIGN KEY (professor_id) REFERENCES professores(id) 
        )
        ''')
        return conexao, cursor
    except sqlite3.OperationalError as e:
        print(f"ERROR: erro operacional com a tabela... {e}")
        return None, None

def cadastrar_aluno(cursor, conexao):
    try:
        print("--- CADASTRAR ALUNO ---")
        try:
            id_prof = int(input("Qual o ID do seu professor: "))
        except ValueError:
            print("O ID precisa ser um número inteiro.")
            return

        cursor.execute(f"SELECT id FROM professores WHERE id = {id_prof}")
        if not cursor.fetchone():
            print("ERRO: ID do professor não existe!")
            return

        cpf = input("CPF: ")
    
        cursor.execute(f"SELECT id FROM alunos WHERE cpf = '{cpf}'")
        if cursor.fetchone():
            print("Erro: Este CPF já está cadastrado!")
            return

        nome = input("Nome: ")
        telefone = input("Telefone: ")
        turma = input("Turma: ")

        try:
            idade = int(input("Idade: "))
        except ValueError:
            print("A idade precisa ser um número inteiro")
            return
        
        endereco = input("Endereço: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
    
        comando = f'''
        INSERT INTO alunos (nome, telefone, turma, idade, cpf, professor_id, endereco, cidade, estado) 
        VALUES ('{nome}', '{telefone}', '{turma}', {idade}, '{cpf}', {id_prof}, '{endereco}', '{cidade}', '{estado}')
        '''
        cursor.execute(comando)
        conexao.commit()
        print("Aluno cadastrado com sucesso!")

    except sqlite3.IntegrityError as e:
        print(f"Erro de integridade (Ex: CPF duplicado ou restrição de chave): {e}")
    except sqlite3.OperationalError as e:
        print(f"Erro de sintaxe SQL ou tabela ausente: {e}")
    except Exception as e:
        print(f"Erro desconhecido ao cadastrar aluno: {e}")

def listar_alunos(cursor):
    try:
        print("--- LISTA DE ALUNOS ---")
        cursor.execute("SELECT * FROM alunos")
        todos_alunos = cursor.fetchall()
    
        if not todos_alunos:
            print("Nenhum aluno cadastrado!")
            return False
    
        for aluno in todos_alunos:
            print(f"ID: {aluno[0]} | Nome: {aluno[1]} | Telefone: {aluno[2]} | Turma: {aluno[3]} | Idade: {aluno[4]} | CPF: {aluno[5]} | ID Prof: {aluno[6]} | Endereço: {aluno[7]} | Cidade: {aluno[8]} | Estado: {aluno[9]}")
        return True
    except sqlite3.Error as e:
        print(f"Erro ao listar alunos: {e}")
        return False
    except Exception as e:
        print(f"Erro inesperado ao listar: {e}")
        return False

def editar_aluno(cursor, conexao):
    try:
        print("--- EDITAR ALUNO ---")
        if not listar_alunos(cursor):
            return

        try:
            id_aluno = int(input("Digite o ID do aluno que deseja editar: "))
        except ValueError:
            print("O ID do aluno precisa ser um número inteiro.")
            return
        
        cursor.execute(f"SELECT * FROM alunos WHERE id = {id_aluno}")
        if not cursor.fetchone():
            print("Erro: ID não encontrado!")
            return

        try:
            novo_id_prof = int(input("Novo ID do Professor: "))
        except ValueError:
            print("O ID do professor precisa ser um número inteiro.")
            return
        
        cursor.execute(f"SELECT id FROM professores WHERE id = {novo_id_prof}")
        if not cursor.fetchone():
            print("Erro: Novo ID do professor não existe!")
            return

        novo_cpf = input("Novo CPF: ")
        
        cursor.execute(f"SELECT id FROM alunos WHERE cpf = '{novo_cpf}' AND id != {id_aluno}")
        if cursor.fetchone():
            print("Erro: Este novo CPF já pertence a outro aluno!")
            return

        novo_nome = input("Novo Nome: ")
        novo_telefone = input("Novo Telefone: ")
        nova_turma = input("Nova Turma: ")
        
        try:
            nova_idade = int(input("Nova Idade: "))
        except ValueError:
            print("A idade precisa ser um número inteiro.")
            return
            
        novo_endereco = input("Novo endereço: ")
        nova_cidade = input("Nova cidade: ")
        novo_estado = input("Novo estado: ")

        comando = f'''
        UPDATE alunos 
        SET nome = '{novo_nome}', 
            telefone = '{novo_telefone}', 
            turma = '{nova_turma}', 
            idade = {nova_idade}, 
            cpf = '{novo_cpf}', 
            professor_id = {novo_id_prof},
            endereco = '{novo_endereco}',
            cidade = '{nova_cidade}',
            estado = '{novo_estado}'
        WHERE id = {id_aluno}
        '''
        cursor.execute(comando)
        conexao.commit()
        print("Aluno actualizado com sucesso!")
        
    except sqlite3.IntegrityError as e:
        print(f"Erro de integridade ao editar: {e}")
    except sqlite3.OperationalError as e:
        print(f"Erro de sintaxe SQL ao editar: {e}")
    except Exception as e:
        print(f"Erro inesperado ao editar: {e}")

def excluir_aluno(cursor, conexao):
    try:
        print("\n--- EXCLUIR ALUNO ---")
        if not listar_alunos(cursor):
            return

        try:
            id_aluno = int(input("Digite o ID do aluno que deseja excluir: "))
        except ValueError:
            print("O ID do aluno precisa ser um número inteiro.")
            return
        
        cursor.execute(f"SELECT * FROM alunos WHERE id = {id_aluno}")
        if not cursor.fetchone():
            print("Erro: ID não encontrado!")
            return

        comando = f"DELETE FROM alunos WHERE id = {id_aluno}"
        cursor.execute(comando)
        conexao.commit()
        print("Aluno removido com sucesso!")
        
    except sqlite3.Error as e:
        print(f"Erro no banco de dados ao excluir: {e}")
    except Exception as e:
        print(f"Erro inesperado ao excluir: {e}")

conexao, cursor = conectar()

if conexao and cursor:
    while True:
        print("\n---MENU ESCOLA---")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Atualizar Aluno")
        print("4. Excluir Aluno")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_aluno(cursor, conexao)
        elif opcao == '2':
            listar_alunos(cursor)
        elif opcao == '3':
            editar_aluno(cursor, conexao)
        elif opcao == '4':
            excluir_aluno(cursor, conexao)
        elif opcao == '0':
            break
        else:
            print("Opção inválida! Tente novamente.")

    conexao.close()
