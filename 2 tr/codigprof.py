import json #importa a biblioteca de comandos do json
import os#importa a biblioteca de comandos do os

BANCO_DADOS = 'alunos.json'#da um nome ao arquivo json

def cadastrar():#define uma função
    print("\n--- Novo Cadastro ---")#mostra o que tem entre parênteses
    
    if os.path.exists(BANCO_DADOS):#condição para previnir erro
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f:#abre o arquivo no modo de leitura
            alunos = json.load(f)#carrega os dados do arquivo dentro de uma variável
    else:#executa qualquer coisa que nao seja cumprida pelo if
        alunos = []#cria uma lista

    novo_aluno = {#cria uma lista de json
        "nome": input("Nome: "),#pede um valor ao campo do nome da lista
        "telefone": input("Telefone: "),#pede um valor ao campo do telefone da lista
        "turma": input("Turma: "),#pede um valor ao campo da turma da lista
        "idade": int(input("Idade: ")),#pede um valor ao campo da idade da lista
        "cpf": input("CPF: ")#pede um valor ao campo do cpf da lista
    }#fecha a lista
    
    alunos.append(novo_aluno)#adiciona a lista em formato json para a lista de formato python para futuras ações

    with open(BANCO_DADOS, 'w', encoding='utf-8') as f:#abre o arquivo no modo sobesrever
        json.dump(alunos, f, indent=4, ensure_ascii=False)#altera o arquivo json
        
    print("Aluno cadastrado com sucesso!")#mostra o que tem entre parênteses

def listar():#define uma função
    print("\n--- Lista de Alunos ---")#mostra o que tem entre parênteses
    
    if os.path.exists(BANCO_DADOS):#condição para previnir erro
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f:#abre o arquiivo no modo leitura
            alunos = json.load(f)#carrega os dados do arquivo em uma variavel
    else:#executa qualquer coisa que não cumprir os requisítos do if
        alunos = []#cria uma lista no formato de python

    if not alunos:#condição executada se tal item nao existir dentro de alunos
        print("Nenhum aluno cadastrado.")#mostra o que tem entre parênteses
        return#retorna o valor da função à uma variável

    for aluno in alunos:#comando para percorrer uma lista
        print(f"Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}")#mostra o que tem entre parênteses

def atualizar():#define uma função
    print("\n--- Atualizar Aluno ---")#mostra o que tem entre parênteses
    if not os.path.exists(BANCO_DADOS):#condição para previnir erro
        print("Nenhum aluno cadastrado no sistema.")#mostra o que tem entre parênteses
        return#retorna o valor da função à uma variável

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f:#abre o arquiivo no modo leitura
        alunos = json.load(f)#carrega os dados do arquivo em uma variavel
        
    cpf_busca = input("Digite o CPF do aluno que deseja editar: ")#pede o usuário para dar um valor a variável
    
    for aluno in alunos:#comando para percorrer a lista
        if aluno['cpf'] == cpf_busca:#condição de comparação
            print(f"Editando dados de: {aluno['nome']}")#mostra o que tem entre parênteses
            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome']#pede um valor ao campo do nome
            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone']#pede um valor ao campo do telefone
            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma']#pede um valor ao campo da turma
            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade'])#pede um valor ao campo da idade
            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf']#pede um valor ao campo do cpf
            
            with open(BANCO_DADOS, 'w', encoding='utf-8') as f:#abre o arquivo no modo sobesrever
                json.dump(alunos, f, indent=4, ensure_ascii=False)#altera o arquivo json
            print("Dados atualizados com sucesso!")#mostra o que tem entre parênteses
            return#retorna o valor da função à uma variável
            
    print("Aluno não encontrado.")#mostra o que tem entre parênteses

def excluir():#define uma função
    print("\n--- Excluir Aluno ---")#mostra o que tem entre parênteses
    if not os.path.exists(BANCO_DADOS):#condição para previnir erro
        print("Nenhum aluno cadastrado no sistema.")#mostra o que tem entre parênteses
        return#retorna o valor da função à uma variável

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f:#abre o arquiivo no modo leitura
        alunos = json.load(f)#carrega os dados do arquivo em uma variavel
        
    cpf_busca = input("Digite o cpf do aluno que deseja remover: ")#pede um valor a variavel
    
    nova_lista = [a for a in alunos if a['cpf'] != cpf_busca]#define uma lista com comando de percorrimento e uma condição de diferença
    
    if len(nova_lista) < len(alunos):#condição que compara tamanho de listas para ser executada
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:#abre o arquivo no modo sobesrever
            json.dump(nova_lista, f, indent=4, ensure_ascii=False)#altera o arquivo json
        print("Aluno removido com sucesso!")#mostra o que tem entre parênteses
    else:#executa qualquer coisa que não cumprir os requisítos do if
        print("Aluno não encontrado.")#mostra o que tem entre parênteses

def menu():#define uma função
    if not os.path.exists(BANCO_DADOS):#condição para previnir erro
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:#abre o arquivo no modo sobesrever
            json.dump([], f)#altera o arquivo json

    while True:#loop de execução
        print("\n=== SISTEMA ESCOLAR ===")#mostra o que tem entre parênteses
        print("1. Cadastrar Aluno")#mostra o que tem entre parênteses
        print("2. Listar Alunos")#mostra o que tem entre parênteses
        print("3. Atualizar Aluno")#mostra o que tem entre parênteses
        print("4. Excluir Aluno")#mostra o que tem entre parênteses
        print("5. Sair")#mostra o que tem entre parênteses
        
        opcao = input("Escolha uma opção: ")#pede um valor a variável
        
        if opcao == '1': cadastrar()#condição de comparação para escolha de ação
        elif opcao == '2': listar()#condição de comparação para escolha de ação
        elif opcao == '3': atualizar()#condição de comparação para escolha de ação
        elif opcao == '4': excluir()#condição de comparação para escolha de ação
        elif opcao == '5': break#condição de comparação para escolha de ação
        else: print("Opção inválida!")#executa qualquer coisa que não cumprir os requisítos do if

menu()#executa a função principal responsável por mostrar as opções de ações que o programa realiza