distancia = float (input('Informe a distancia da viagem: '))
if distancia <= 200:
    total = distancia * 0.50
else:
    total = distancia * 0.45
print (f'O valor a ser pago pela viagem é de {total:.2f}')