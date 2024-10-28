print('Média', 20)

resp = 's'
media = qnt = maior = menor = total = 0
while resp in 'Ss':
    n = int(input('Número inteiro: '))
    qnt += 1
    total = n + total
    if qnt == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quem continuar [S / N] ')).upper().strip()
media = total / qnt
print(f'Você digitou {qnt} números e a média é {media}')
print(f'O maior número é {maior} e o menor é {menor}')
