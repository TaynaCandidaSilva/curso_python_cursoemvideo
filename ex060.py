num = int (input('Informe um número: '))
fatorial = 1
contador = num
print(f'Calculando {num}! = ', end='')

while contador > 0:
    print(f'{contador}', end='')
    print(' X ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1
print(fatorial)

    
    