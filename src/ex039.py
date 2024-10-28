print ('--------------Informações sobre alistamento---------------------')
from datetime import date
atual = date.today().year
sexo = str(input('Informe seu sexo M/F: ')).upper()
if sexo == 'M':
    nasc = int(input('Informe seu ano de nascimento: '))
    idade = atual - nasc
    if idade == 18:
        print ('Você deve se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        print(f'Ainda FALTAM {saldo} ANOS para o alistamento')
        ano = (f'Seu alistamento será em {atual + saldo}')
    elif idade > 18:
        saldo = idade - 18
        print (f'Você JÁ DEVERIA TER SE ALISTADO há {idade-18} anos')
        print (f'Seu alistamento foi em {atual - saldo}')
else:
    print('Você não tem obrigatóriedade de alistamento')
