n = str(input('digite um número: '))
print (f'milhar: {n[0]}')
print (f'centenas: {n[1]}')
print (f'dezenas: {n[2]}')
print (f'unidades: {n[3]}')

num = int(input('Infome um número: '))
m = num //1000 % 10
c = num //100 % 10
d = num //10 % 10
u = num //1 % 10
print (f'Analisando o número {num}...')
print (f'milhar: {m}')
print (f'centenas: {c}')
print (f'dezenas: {d}')
print (f'unidades: {u}')