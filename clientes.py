clientes = []
def cadastrar():
    print('cadastrando')
    nome = input('Digite o nome')
    telefone = input('Digite o telefone')
    cliente = [nome, telefone]
    clientes.append(cliente)

def listar():
    print('listando')
    print(f'{"nome":^10}\t{"telefone":^10}')
    for cliente in clientes:
        print(f'{cliente[0]:10}\t{cliente[1]:10}')

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