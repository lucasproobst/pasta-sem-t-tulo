n1 = int(input('Numero: '))
n2 = int(input('Numero: '))

def somar():
    print(f'Resultado da soma: {n1 + n2}')

def subtrair():
    print(f'Resultado da soma: {n1 - n2}')

def dividir():
    print(f'Resultado da soma: {n1 / n2}')

def porcentagem():
    print(f'Resultado da soma: {(n1 + n2) / 100}')

def menu():
    try:
        print('''
            [+] - Somar
            [-] - Subtrair
            [/] - Dividir
            [%] - Porcentagem
            [S] - Sair''')
        
        opcao = input('Opcao: ')
    except ValueError:
        print('Opcao invalida.')

    match opcao:
        case '+':
            somar()
        case '-':
            subtrair()
        case '/':
            dividir()
        case '%':
            porcentagem()
        case 'S':
            pass

menu()