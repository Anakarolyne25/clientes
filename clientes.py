NOME_ARQUIVO = "clientes.txt"
clientes = []
def cadastrar():
    print('cadastrando')
    nome = input('Digite o nome : ')
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
    arquivo = open(NOME_ARQUIVO, "a")
    arquivo.write(f'{cliente[0]} {cliente[1]}\n')
    arquivo.close()

def buscarClientesArquivo():
    arquivo = open(NOME_ARQUIVO, "r") 
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