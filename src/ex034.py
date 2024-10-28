salario = float (input('Informe o seu salário R$: '))
if salario <= 1250 :
    novo = salario * 1.15
else:
    novo = salario * 1.10
print (f'Quem ganhava R$ {salario:.2f} passará a receber R$ {novo:.2f} ')