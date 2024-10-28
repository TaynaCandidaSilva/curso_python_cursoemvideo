listanum = []
mai = 0
men = 0
for n in range(0,5):
   listanum.append(int(input(f'Digite um valor para a Posição {n}:')))
   if n == 0:
       mai = men = listanum[n]
   else:
       if listanum[n] > mai:
           mai = listanum[n]
        
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...', end='')
print()