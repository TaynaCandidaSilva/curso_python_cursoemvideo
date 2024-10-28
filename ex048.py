soma = 0
cont = 0
for num in range (1, 501):
    if num % 2 != 0 and  num % 3 == 0:
        cont = cont +1
        soma += num
print (f'A soma dos {cont} números ímpares múltiplos de 3 de 1 a 500 é: {soma}')
    
