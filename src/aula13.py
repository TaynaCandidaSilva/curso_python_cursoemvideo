i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p): #Para c (variável) em intervalo (início, fim, passo)
    print(c)
  
    
for n in range(0, 3):
     n = int(input('Digite um número: '))
print('Fim')


s = 0
for c in range(0, 3):
    n = int (input('Digite um valor: '))
    s += n
print(f'A soma de todos os números é: {s}')