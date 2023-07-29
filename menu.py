# nome = input ('Qual o seu primeiro nome? ' )
# snome = input ('Qual o seu sobre nome? ' )
# idade = input ('Qual a sua idade? ')

# print ('Seu nome completo é: {}.\n Seu sobre nome é: {}.\n e sua idade é: {}' .format(nome, snome, idade))


# print('[1] Escrever nome \n[2] Escrever Sobrenome \n[3] Escrever a idade')

# if input == 1:
#     print('Qual o seu nome? ')

def menu_opcoes():
    print('[1] Escrever nome')
    print('[2] Escrever Sobrenome')
    print('[3] Escrever a idade')

def preencher_nome():
    nome = input('Digite o nome: ')
    # Faça o que desejar com o nome (ex: salvar em uma variável global)

def preencher_sobrenome():
    sobrenome = input('Digite o sobrenome: ')
    # Faça o que desejar com o sobrenome (ex: salvar em uma variável global)

def preencher_idade():
    idade = input('Digite a idade: ')
    # Faça o que desejar com a idade (ex: salvar em uma variável global)

def main():
    while True:
        menu_opcoes()
        opcao = input('Escolha uma opção (ou digite "sair" para encerrar): ')

        if opcao == '1':
            preencher_nome()
        elif opcao == '2':
            preencher_sobrenome()
        elif opcao == '3':
            preencher_idade()
        elif opcao.lower() == 'sair':
            break
        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')

if __name__ == "__main__":
    main()

