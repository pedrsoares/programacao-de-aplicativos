import sqlite3

try:
    conexao = sqlite3.connect('escola.demonstracao.db')
    cursor = conexao.cursor()
except sqlite3.Error as erro:
    print(f"Erro ao conectar ao banco de dados: {erro}")
    exit()



def cadastrar_professor():
    try:
        nome_completo = input("Digite o nome completo: ")
        telefone_professor = input("Digite o telefone: ")
        materia = input("Digite a Matéria: ")
        idade_professor = int(input("Digite a idade: "))
        cpf = input("Digite o CPF: ")
        salario = input("Digite seu salário: ")
        escola = input("Digite o nome da escola: ")
        endereco = input("Digite o endereço: ")

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS professores(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT, 
            materia TEXT, 
            idade INTEGER,
            cpf TEXT UNIQUE NOT NULL,
            salario TEXT NOT NULL,
            escola TEXT,
            endereco TEXT
        )
        ''')

        comando_inserir = f'''
        INSERT INTO professores(nome, telefone, materia, idade, cpf, salario, escola, endereco)
        VALUES('{nome_completo}', '{telefone_professor}', '{materia}', {idade_professor}, '{cpf}', '{salario}', '{escola}', '{endereco}')'''

        cursor.execute(comando_inserir)
        conexao.commit()
        print("Professor cadastrado com sucesso!")

    except ValueError:
        print("Erro: A idade deve ser um número inteiro válido.")
    except sqlite3.IntegrityError:
        print("Erro: Já existe um professor cadastrado com este CPF.")
    except sqlite3.Error as erro:
        print(f"Erro no banco de dados ao cadastrar: {erro}")




def listar():
    try:
        cursor.execute("SELECT * FROM professores")
        linhas = cursor.fetchall()
        
        if not linhas:
            print("Nenhum professor cadastrado.")
        else:
            for linha in linhas:
                print(f"ID: {linha[0]} | Nome: {linha[1]} | Matéria: {linha[3]} | CPF: {linha[5]}")
        print("\n")
    except sqlite3.Error as erro:
        print(f"Erro ao listar professores: {erro}")



def atualizar():
    try: 

        id_professor = int(input("Qual é o teu ID: "))

        cursor.execute(f'''SELECT * FROM professores WHERE id = {id_professor}''')
        professores = cursor.fetchone()

        if profesores is None:
            print("Não encontrado!")
        else:
            novo_nome = input("qual o novo nome: ")
            novo_telefone = input("qual o novo telefone: ")
            novo_materia = input("qual a nova materia: ")
            novo_idade = int(input("qual a nova idade: "))
            novo_cpf = input("qual o novo cpf: ")
            novo_salario = float(input("qual o novo salario: "))
            novo_nome_de_escola = input("qual o novo nome da escola: ")

            comando = f'''UPDATE professores SET nome = '{novo_nome}',telefone = '{novo_telefone}',materia = '{novo_materia}',idade = {novo_idade},cpf = '{novo_cpf}',salario = {novo_salario},escola = '{novo_nome_de_escola}' WHERE id ={id_professor}'''
            
            cursor.execute(comando)
            conexao.commit()
            print("Dados atualizados com sucesso!")


    except ValueError:
        print("Valor invalido")

    except TypeError:
        print("Tipo de dado invalido") 

    except ZeroDivisionError:
        print("Divisão por zero")

    except FileNotFoundError:
        print("Arquivo não encontrado")

    except Exception as erro:
        print(f"Ocorreu um erro: {erro}")	

    finally:
        print("Codigo encerrado")



def excluir():
    try:
        id_professor = int(input("Digite o ID do professor que deseja excluir: "))
        
        cursor.execute(f"SELECT * FROM professores WHERE id = {id_professor}")
        professor_existe = cursor.fetchone()

        if professor_existe is None:
            print("Nenhum professor encontrado com esse ID.")
        else:
            cursor.execute(f"DELETE FROM professores WHERE id = {id_professor}")
            conexao.commit()
            print("Professor excluído com sucesso.")
            
    except ValueError:
        print("Erro: O ID precisa ser um número inteiro.")
    except sqlite3.Error as erro:
        print(f"Erro ao excluir registro: {erro}")




def menu():
    while True:
        try:
            print("\n1. Cadastrar Professor")
            print("2. Listar Professores")
            print("3. Alterar Professor")
            print("4. Excluir Professor")
            print("5. Sair")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == '1':
                cadastrar_professor()
            elif opcao == '2':
                listar()
            elif opcao == '3':
                atualizar()
            elif opcao == '4':
                excluir()
            elif opcao == '5':
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida.")
                
        except KeyboardInterrupt:
            print("\n\nExecução interrompida. Fechando o sistema de forma segura...")
            break
        except Exception as erro:
            print(f"Ocorreu um erro inesperado no menu: {erro}")
            
    try:
        conexao.close()
    except:
        pass


menu()
