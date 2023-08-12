# valorHamburguer = float(input())
# quantidadeHamburguer = int(input())
# valorBebida = float(input())
# quantidadeBebida = int(input())
# valorPago = float(input())

# # TODO: Calcular o preço final do pedido (total dos hambúrgueres + total das bebidas).

# total_pedido = (valorHamburguer * quantidadeHamburguer) + (valorBebida * quantidadeBebida)


# # TODO: Calcular o troco do pedido, considerando o preço final e o valor pago pelo usuário.

# troco = float(valorPago - total_pedido)

# # TODO: Imprimir a saída no formato especificado neste desafio.

# print(f'O preço final do pedido é R$ {total_pedido:.2f}. Seu troco é R$ {troco:.2f}')

############################ ##  Sobremesa ## ###########################################

# valorPedido = int(input())

# # TODO: Criar as condições necessárias para impressão da saída conforme o enunciado.

# if valorPedido >= 50:
#     print('Parabens, você ganhou uma sobremesa gratis!')
# else:
#     print ('Que pena, você nao ganhou nenhum brinde especial.')


######################################## ##  #  ## ###########################################

################################### ##  Valor Pedido ## ####################################

#  Desconto
# 4
# Pizza 19.99 Salada 29.99 Sushi 61.00 Pudim 10.00
# 20%
# Saída esperada:
# Valor total: 96.78

# def main():
#     n = int(input())
 
#     total = 0
 
#     for i in range(1, n + 1):
#         pedido = input().split(" ")
#         nome = pedido[0]
#         valor = float(pedido[1])
#         total += valor
 
#     desconto = input()
#     if desconto == '10%':
#         desconto = total * 0.1
#         total -= desconto
#     elif desconto == '20%':
#         desconto = total * 0.2
#         total -= desconto
          
#         print(f'Valor total: {total}')

          
#   # TODO: Criar as condições para aplicar o cupom de desconto (10% ou 20%).
 
 
# if __name__ == "__main__":
#     main()
    

######################################## ##  #  ## ###########################################

######################################## ##  Restaurante vegano  ## ###########################################

# Pedido 1: Pizza (Nao-vegano) - 450 calorias

# Pedido 2: Sushi (Nao-vegano) - 200 calorias



numPedidos = int(input('qual pedido?'))

for i in range(1, numPedidos + 1):
    prato = input('Qual o prato? ')
    calorias = int(input('quantas calorias? '))
    ehVegano = input('É vegano? ')

pedido_1 = (prato, calorias, ehVegano,)
pedido_2 = (prato, calorias, ehVegano,)

if ehVegano == 's':
    tipo= 'Vegano'
else:
    tipo = 'Não-vegano'

if numPedidos == 1:
    print(pedido_1)
 
if numPedidos == 2:
    print(pedido_2)
# print(f'Pedido 1:{prato} ({(tipo)}) - {calorias} calorias')


    # print(f'Pedido 1:{prato} ({(tipo)}) - {calorias} calorias')

    # print(f'Pedido 2:{prato} ({(tipo)}) - {calorias} calorias')


# checando tipo de pedido 1
# if i == 1 and ehVegano == 's':
#     print(f'Pedido 1:{prato} ({(prato_vegano)}) - {calorias} calorias')
# elif i == 1 and ehVegano == 'n':
#     print(f'Pedido 1:{prato} ({(prato_nãp_vegano)}) - {calorias} calorias')
    
# elif numPedidos == 2:
# elif i == 2 and ehVegano == 's':

#     print(f'Pedido 1:{prato} ({(prato_vegano)}) - {calorias} calorias \n \nPedido 2:{prato} ({(prato_vegano)}) - {calorias} calorias')
        
#     prato2 = input()
#     calorias2 = int(input())
#     ehVegano = input()

#     print(f'Pedido 1:{prato} ({(msg)}) - {calorias} calorias \n \nPedido 2:{prato2} ({(msg)}) - {calorias2} calorias')




   


      