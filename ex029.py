vel = float(input('Informe a sua velocidade atual: '))
if vel > 80:
    print ('Você ultrapasou a velocidade máxima permitida e será multado!')
    multa = (vel - 80) * 7
    print (f'Você deverá pagar R$ {multa:.2f} de multa por ultrapassar a velocidade máxima permitida!') 
else:
    print ('Você está dentro da velocidade máxima permitida!')
