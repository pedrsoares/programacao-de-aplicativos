import sqlite3
conexao = sqlite3.connect('escola.demonstracao.db')
cursor = conexao.cursor()

def cadastrar_aluno():
    nome_completo_aluno = input("Digite o nome completo: ")
    telefone_aluno = input("Digite o telefone: ")
    turma_aluno = input("Digite a Turma: ")
    idade_aluno = int(input("Digite a idade: "))
    cpf_aluno = input("Digite o cpf: ")
    professor_id = int(input("Digite o ID do professor: "))

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS alunos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT, 
                turma TEXT, 
                idade INTEGER,
                cpf TEXT UNIQUE NOT NULL,
                professor_id INTEGER,
                FOREIGN KEY (professor_id) REFERENCES professores(id))''')
    comando_inserir = f'''
        INSERT INTO alunos(nome, telefone, turma, idade, cpf, professor_id)
        VALUES('{nome_completo_aluno}', '{telefone_aluno}', '{turma_aluno}', '{idade_aluno}', '{cpf_aluno}', {professor_id})'''

    cursor.execute(comando_inserir)
    conexao.commit()

def listar():
    conexao.commit()
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    for aluno in alunos:
        print(f"{aluno[0]}, nome: {aluno[1]}, telefone: {aluno[2]}, turma: {aluno[3]}, idade: {aluno[4]}, CPF: {aluno[5]}, professor: {aluno[6]}")
    print("\n")

def buscar():
    id_aluno = int(input("Digite o id do aluno: "))
    cursor.execute("SELECT * FROM alunos WHERE id = ?", (id_aluno))

    aluno = cursor.fetchone()
    if aluno:
        print("Aluno encontrado ")
        print(aluno)

    else:
        print("Aluno não encontrado")

def atualizar():
    id_aluno = int(input("Digite o id do aluno: "))
    novo_nome = input("Digite o novo nome: ")
    novo_telefone = input("Digite o novo telefone: ")
    nova_turma = input("Digite a nova turma: ")
    nova_idade = int(input("Digite a nova idade: "))
    novo_cpf = input("Digite o novo CPF: ")
    novo_professor = int(input("Digite o ID do novo professor: "))

    cursor.execute(f'''
                   UPDATE alunos
                    SET nome = '{novo_nome}', telefone = '{novo_telefone}',turma = '{nova_turma}', idade = {nova_idade}, cpf = '{novo_cpf}', professor_id = {novo_professor} WHERE id = {id_aluno}''')
    conexao.commit()
    print("Dados atualizados com sucesso! ")


def remover():
    id_aluno = int(input("Digite o ID do aluno que deseja remover: "))
    cursor.execute(
        "DELETE FROM alunos WHERE id = ?", (id_aluno,)
    )

    conexao.commit()
    if cursor.rowcount > 0 :
        print("Aluno removido com sucesso.")
    else:
        print("Nenhum aluno encontrado com esse ID. ")

opcao_while = 0
while True:
    print("1 - CADASTRAR ALUNO\n2 - LISTAR ALUNOS\n3 - BUSCAR ALUNO\n4 - ATUALIZAR DADOS\n5 - EXCLUIR CADASTRO\n6 - FECHAR PROGRAMA ")
    opcao_while = int(input("Qual ação deseja realizar: "))
    if opcao_while == 1:
        cadastrar_aluno()
    elif opcao_while == 2:
        listar()
    elif opcao_while == 3:
        buscar()
    elif opcao_while == 4:
        atualizar()
    elif opcao_while == 5:
        remover()
    elif opcao_while == 6:
        conexao.close()
        break