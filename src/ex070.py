totalcompra = totalmais1000  = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço do produto R$: '))    
    cont +=1
    totalcompra += preco
    if preco > 1000:
        totalmais1000 +=1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    else: 
        if preco < menor:
            menor = preco
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S/N]')).upper().strip()
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total gasto foi de R$ {totalcompra} ')
print(f'Produtos que custam mais de 1000: {totalmais1000} ')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
    

            
    



