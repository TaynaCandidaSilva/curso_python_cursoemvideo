lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n) 
    resp = str(input('Quer continuar [S/N] '))
    if resp in 'Nn':
        break
print(f'Foram digitados {len(lista)} números')
lista.sort(reverse=True)
print(f'Lista com valores descrescente são {lista}')
if 5 in lista:
    print('O número 5 FAZ PARTE da lista!')
else:
    print('O número 5 NÃO FAZ parte da lista')
    
    
