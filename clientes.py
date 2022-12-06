NOME_ARQUIVO = "clientes.txt"
clientes = []
def cadastrar(nome_arquivo):
    print('cadastrando')
    nome = input('Digite o nome')
    telefone = input('Digite o telefone')
    cliente = [nome, telefone]
    salvarArquivo(cliente, nome_arquivo)

def salvar(cliente, clientes):
    clientes.append(cliente)

def buscarClientes():
    return clientes

def listar():
    clientes = buscarClientesArquivo()
    print('listando')
    print(f'id {"nome":^10}\t{"telefone":^10}')
    for id, cliente in enumerate(clientes):
        print(f'{id} {cliente[0]:10}\t{cliente[1]:10}')

def salvarArquivo(cliente, nome_arquivo):
    arquivo = open(nome_arquivo, "a")
    arquivo.write(f'{cliente[0]};{cliente[1]}\n')
    arquivo.close()

def buscarClientesArquivo():
    clientes = []
    arquivo = open(NOME_ARQUIVO, "r") 
    for linha in arquivo: 
        cliente = linha.strip().split(';')
        clientes.append(cliente)
    arquivo.close()
    return clientes
      
def alterar():
    listar()
    id = int(input('Digite o id da linha que deseja alterar: '))
    cliente = buscarCliente(id)
    novo_nome = input(f'Digite o novo nome: [{cliente[0]}] ')
    novo_telefone = input(f'Digite o novo telefone [{cliente[1]}]: ')
    if novo_nome != '':
        cliente[0] = novo_nome
    if novo_telefone != '':
        cliente[1] = novo_telefone
    editar(id, cliente)

def editar(id, cliente):
    print(f'Alterando valor do cliente #{id} para: {cliente}')

def buscarCliente(id):
    clientes = buscarClientesArquivo()
    cliente = clientes[id]

    return cliente

while True:
    print('1.Cadastrar')
    print('2.Listar')
    print('3.Alterar')
    print('4.Sair')
    opcao = int(input('Qual das opções desejada?'))
    if opcao == 1:
        cadastrar(NOME_ARQUIVO)
    elif opcao == 2:
        listar()
    elif opcao == 3:
        alterar()
    else: 
        print('exit')
        break 