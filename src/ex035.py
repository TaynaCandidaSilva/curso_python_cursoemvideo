print ('--------------------Analisador de triângulos-----------------------------')
r1 = float(input('1° seguimento: '))
r2 = float(input('2° seguimento: '))
r3 = float(input('3° seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print ('Os seguimentos PODEM formar um triângulo ', end='')
    if r1 == r2 == r3:
        print ('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print ('ESCALENO!')
    else:
        print('ISÓSCELES')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR um triângulo!')