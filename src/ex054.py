from datetime import date
atual = date.today().year
maior = 0
menor = 0
for i in range (1, 3):
    nasc = int(input(f'Digite o ano de nascimento: '))
    idade = atual - nasc
    if idade >=21:
        maior += 1
    else:
        menor += 1

print (f'{maior} pessoas já atingiram a maioridade')
print (f'{menor} pessoas NÃO ATINGIRAM a maioridade')