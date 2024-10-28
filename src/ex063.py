# print('-^'*11)
# print('SEQUÊNCIA DE FIBONACCI')
# print('-^'*11)
# sequencia = [0, 1]
# proximo = 0
# cont = 0

# f_n = int(input('Quantos termos você gostaria de ver: '))

# while cont < f_n-2:
#     proximo = sequencia[-1] + sequencia[-2]
#     sequencia.append(proximo)
#     cont +=1
# print(sequencia)
  


n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' -> {t3} ', end='')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
