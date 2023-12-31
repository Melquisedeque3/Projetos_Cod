
menu = """
======== Menu ========
|                    |
|    [d] depositar   |
|    [s] sacar       |
|    [e] extrato     |
|    [q] sair        |
|                    |
DioBank===============
"""

saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'e':
        extratos()
    
    elif opcao == 'd':
        deposito = float(input('\nQuanto deseja depositar? \n'))

        # Operação de depósito:
        if deposito > 0:
            saldo += deposito
            extrato += f"Deposito: R${deposito:.2f}\n"
            print('\nDeposito realizado com sucesso.\n ')

            # Deposito não realizado
        else:
            print('Não foi possível realizar a operação, \n  \n     Deposite um valor válido.')       
       
    elif opcao == 's':
        
        saque = float(input('Quanto deseja sacar? '))
        
        # Verificações:
        sem_saldo = saque > saldo
        sem_limite = saque > limite
        sem_limite_saque = numero_saques == LIMITE_SAQUES

        # Operações não realizadas:

        if sem_saldo:
            print('Não foi possível realizar essa operação,\nVocê não tem saldo suficiente para sacar.\nVá na opção: [d]depositar e deposite um valor válido.')

        elif sem_limite:
            print('Não foi possível realizar essa operação,\nInsira um valor igual ou menos que o seu limite.')
            
        elif sem_limite_saque:
            print('Não foi possível realizar essa operação,\nVocê exedeu o limite de saques diário. \nTende novamente amanhã.')
      
        else: 
            # Saque realizado
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_saques += 1
            print('Saque realizado com sucesso')
    
    elif opcao == 'q':
        break

    else: 
        print ('Opção inválida, por favor digite novamente a opção desejada')


def extratos():
            
    ms_extrato = f"Seu saldo atual é de R$ {saldo:.2f}\n"
            
            # Resumo de depositos e saques
    print('=============== Extrato =============== \n')
    print('| Operações não realizadas             |\n' if not extrato else extrato)
    print(ms_extrato)
    print('DioBank================================ ')
