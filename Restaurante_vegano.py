numPedidos = int(input())

pedidos = []

for i in range(1, numPedidos + 1):
    prato = input()
    calorias = int(input())
    ehVegano = input()

    if ehVegano == 's':
        tipo = 'Vegano'
    else:
        tipo = 'Não-vegano'
    
    pedido = (prato, calorias, tipo)
    pedidos.append(pedido)

for i, pedido in enumerate(pedidos, start=1):
    prato, calorias, tipo = pedido
    print(f'Pedido {i}: {prato} ({tipo}) - {calorias} calorias')
