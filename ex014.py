c = float(input('informe a temperatura em celsius: '))
f = c*1.8+32
print (f'{c}°C convertidos para Fahrenheit resulta em {f}°F')

dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km foram percorridos? '))
valor = (60*dias) + km * 0.15
print (f'O valor total a ser pago pelo aluguel do carro é: R$ {valor:.2f} ')