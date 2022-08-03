NOME_ARQUIVO = "clientes.txt"
clientes = []
def cadastrar():
    print('cadastrando')
    nome = input('Digite o nome : ').capitalize().strip()
    telefone = input('Digite o telefone : ')
    cliente = [nome, telefone]
    salvarArquivo(cliente)

def salvar(cliente):
    clientes.append(cliente)

def buscarClientes():
    return clientes

def listar():
    clientes = buscarClientesArquivo()
    print('listando')
    print(f'{"nome":^10}\t{"telefone":^10}')
    for cliente in clientes:
        print(f'{cliente[0]:10}\t{cliente[1]:10}')

def salvarArquivo(cliente):
    with open(NOME_ARQUIVO, 'a') as arquivo:
        arquivo.write(f'{cliente[0]} {cliente[1]}\n')

def buscarClientesArquivo():
    with open(NOME_ARQUIVO, "r") as arquivo:
        for linha in arquivo:
            print(linha)

while True:
    print('''
    [ 1 ]. Cadastrar
    [ 2 ]. Listar
    [ 3 ]. Sair
    ''')
    opcao = int(input('Qual das opções desejada? '))
    if opcao == 1:
        cadastrar()
    elif opcao == 2:
        listar()
    else: 
        print('exit')
        break 