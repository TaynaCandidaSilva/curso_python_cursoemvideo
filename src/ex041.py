from datetime import date
print ('----------------VERIFICANDO A CATEGORIA DE UM ATLETA------------')
ano = int (input('Qual o ano do seu nascimento? '))
idade = date.today().year - ano
print (f'O atleta tem {idade} anos')
if idade <=9:
    print ('Categoria: MIRIM')
elif idade <=14:
    print ('Categoria: INFANTIL')
elif idade <=19:
    print ('Categoria: JÚNIOR')
elif idade <=25:
    print ('Categoria: SÊNIOR')
else:
    print ('Categoria: MASTER')
   
    