num = int(input('Digite um número inteiro: '))
print ("""Escolha uma das bases para conversão:
[ 1 ] conversão para BINÁRIO
[ 2 ] conversão para OCTAL
[ 3 ] conversão para HEXADECIMAL""")
op = int(input('Sua opção: '))
if op == 1:
    print (f'O número {num} convertido para Binário é {bin(num)[2:]}')
elif op == 2:
    print (f'O número {num} convertido para Octal é {oct(num)[2:]}')
elif op == 3:
    print (f'O número {num} convertido para Hexadecimal é {hex(num)[2:]}')
else:
    print('Opção inválida!')