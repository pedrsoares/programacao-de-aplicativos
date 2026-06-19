open('habito.txt', 'w').close()

def criar():
    nome = input("Nome do habito: ")
    with open('habito.txt', 'a') as f:
        f.write(nome + '\n')
    print("Aluno cadastrado!")


def ler():
    with open('habito.txt', 'r') as f:
        alunos = f.readlines()
        
        i = 0
        for aluno in alunos:
            print(f"{i} - {aluno.strip()}") # Strip - Remove espaços em branco e o \n
            i += 1  # Incrementamos 1 para a próxima linha

# nome = "   João Silva\n"
# print(f"Original: '{nome}'")
# print(f"Com strip: '{nome.strip()}'")

def atualizar():
    ler() # Mostra a lista para o usuário escolher
    idx = int(input("Digite o ID do habito que deseja alterar: "))
    novo_nome = input("Novo nome: ")
    
    with open('habito.txt', 'r') as f:
        linhas = f.readlines()
    
    linhas[idx] = novo_nome + '\n' # Altera na lista
    
    with open('habito.txt', 'w') as f: # Sobrescreve com a lista atualizada
        f.writelines(linhas)
    print("Aluno atualizado!")


def deletar():
    ler()
    idx = int(input("Digite o ID do habito que deseja excluir: "))
    
    with open('habito.txt', 'r') as f:
        linhas = f.readlines()
    
    del linhas[idx] # Remove da lista
    
    with open('habito.txt', 'w') as f:
        f.writelines(linhas)
    print("habito removido!")


while True:
    print("\n1-Cadastrar | 2-Listar | 3-Editar | 4-Excluir | 5-Sair")
    opcao = input("Escolha: ")
    
    if opcao == '1': criar()
    elif opcao == '2': ler()
    elif opcao == '3': atualizar()
    elif opcao == '4': deletar()
    elif opcao == '5': break # Interrompe o laço de repetição
