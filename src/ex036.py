valor = float(input('Qual o valor da casa: R$ '))
salario = float(input('Qual o salário: R$ '))
anos = int(input('Em quantos anos será pago: '))
presm = valor/(anos*12)
if presm < salario*0.30:
    print('Empréstimo aprovado, parabéns!')
    print(f'Você pode financiar uma casa de R$ {valor:.2f} em {anos} anos')
    print (f'O valor da parcela será de R$ {presm:.2f}')
else: 
    print('Emprestimo negado!')
    