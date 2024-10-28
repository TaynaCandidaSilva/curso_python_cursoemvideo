valores = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resp = str(input('Quer continuar [S/N] '))
    if resp in 'Nn':
        break
valores.sort()
print(f'Os valores digitados foram {valores}')