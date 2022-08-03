clientes = []

def cadastrar():
    while True:
        print('cadastrando \n')
        nome = input('Digite o nome do cliente : ').capitalize().strip()
        telefone = input('Digite o telefone do cliente : ')
        cliente = [nome, telefone]
        salvarArquivo(cliente)
        if cadastrarNovamente() == False:
            break

def salvarArquivo(cliente):
    with open('contatos.txt', 'a') as arquivo:
        arquivo.write(f'{cliente[0]} {cliente[1]} \n')

def cadastrarNovamente():
    while True:
        continuar = input('Deseja cadastrar outro cliente? [S/N] ').lower().strip()

        if continuar in 'sn':
            if continuar == 's':
                return True
            else:
                return False
        else:
            print('Resposta Inválida!')

def buscarLista():
    return clientes

def listar():
    clientes = buscarLista()
    print('listando')
    print(f'{"nome":^10}\t{"telefone":^10}')
    for cliente in clientes:
        print(f'{cliente[0]:10}\t{cliente[1]:10}')


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
    elif opcao == 3: 
        print('exit')
        break 
    else:
        print('Opção inválida, por favor digite novamente.')