print ('--------------------CALCULADORA DE IMC-------------------')
peso = float(input('Qual é o seu peso (kg): '))
altura = float(input('Qual é a sua altura (m): '))
imc = peso/(altura*altura)
print(f'Seu IMC é: {imc:.2f}')
if imc <18.5:
    print('Você está ABAIXO DO PESO NORMAL')
elif imc <= 24.9:
    print ('Você está SAÚDAVEL')
elif imc <=29.9:
    print ('Você está com SOBREPESO')
elif imc <=34.9:
    print ('Você está com OBESIDADE GRAU 1')
elif imc <=39.9:
    print ('Você está com OBESIDADE GRAU 2 (SEVERA)')
elif imc >=40:
    print ('Você está com OBESIDADE GRAU 3 (MÓRBIDA)')
