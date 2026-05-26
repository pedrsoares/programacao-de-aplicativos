import json
import os 

BANCO_DADOS = 'alunos.json'

def cadrastro_aluno():
    print("\n--- Novo Cadastro ---")

    if os.path.exists(BANCO_DADOS):
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f:
            alunos = json.load(f)
    else:
        alunos = []

    aluno_novo = {
        "nome": input("Nome: "),
        "id": int(input("id: ")),
        "telefone": input("Telefone: "),
        "turma": input("Turma: "),
        "Idade": int(input("idade: ")),
        "cpf": int(input("cpf: ")),
    }

  alunos.append(novo_aluno)

    with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
        json.dump(alunos, f, indent=4, ensure_ascii=False)

    print("Aluno cadastrado com sucesso!")

def listar():
    print("\n--- Lista de Alunos ---")
    if os.path.exists(BANCO_DADOS):
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f:
            alunos = json.load(f)
    else:
        alunos = []

    f not alunos:
        print("Nenhum aluno cadastrado.")
     return

    for aluno in alunos:
        print(f"Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']} | id: {aluno['id']} ")

