from time import sleep
print ('-------------CALCULADORA------------')
n1 = int (input ('Informe um número: '))
n2 = int (input('Informe outro número: '))
opcao = 0
while opcao != 5:
    print ('''\n[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa\n''')
    opcao = int(input('Escolha a opção desejada: '))
    if opcao == 1:
        resultado = n1 + n2
        print (f'{n1} + {n2} é {resultado}')
    elif opcao == 2:
        resultado = n1 * n2
        print (f'{n1} x {n2} é {resultado}')
    elif opcao == 3: 
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior é {maior}')
    elif opcao == 4:
        n1 = int (input ('Informe um número: '))
        n2 = int (input('Informe outro número: '))  
        continue
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida!')
    print('=-=' *10)
sleep(2)
print('Fim do programa!')

        
            
            
