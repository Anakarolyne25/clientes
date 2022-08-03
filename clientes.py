clientes = []
def cadastrar():
    print('cadastrando')
    nome = input('Digite o nome')
    telefone = input('Digite o telefone')
    cliente = [nome, telefone]
    salvarArquivo(cliente)

def salvar(cliente):
    clientes.append(cliente)

def buscarLista():
    return clientes

def listar():
    clientes = buscarLista()
    print('listando')
    print(f'{"nome":^10}\t{"telefone":^10}')
    for cliente in clientes:
        print(f'{cliente[0]:10}\t{cliente[1]:10}')

def salvarArquivo(cliente):
    arquivo = open("contatos.txt", "a")
    arquivo.write(f'{cliente[0]} {cliente[1]}')
    arquivo.close()



while True:
    print('1.cadastrar')
    print('2.listar')
    print('3.sair')
    opcao = int(input('Qual das opções desejada?'))
    if opcao == 1:
        cadastrar()
    elif opcao == 2:
        listar()
    else: 
        print('exit')
        break 