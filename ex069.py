print('-'*25)
print('CADASTRO DE PESSOAS')
print('-'*25)
totalmaior18 = totalhomem = totalmulher20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo [M/F]: ')).upper().strip() 
    if sexo == 'M':
        totalhomem +=1
    if idade < 20 and sexo == 'F':
        totalmulher20 +=1
    if idade > 18:
        totalmaior18 +=1
    resp = ' '
    while resp not in'SN':
        resp = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {totalmaior18}')
print(f'Ao todo temos {totalhomem} homens cadastrados')
print(f'E temos {totalmulher20} mulheres com menos de 20 anos de idade')