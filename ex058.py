from random import randint
computador = randint (0,10)
usuario = int(input('Chute um número entre 0 e 10: '))
acertou = False
cont = 0
while not acertou:
    usuario = int(input('Chute um número entre 0 e 10: '))
    cont +=1
    if computador == usuario:
        acertou = True
    else:
        if usuario < computador:
            print('Mais... Tente mais uma vez')
        elif usuario > computador:
            print('Menos... Tente mais uma vez')       
print ('Parabéns, você acertou')
print (f'Você precisou de {cont} palpites para acertar')
    