maior = 0
menor = 0
for p in range (1, 6):
    peso = float (input(f'Qual o {p}° peso da pessoa: '))
    if p == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print (f'O maior peso é {maior}')
print (f'O menor peso é {menor}')