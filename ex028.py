from random import randint
from time import sleep
print ('----------JOGO: ACERTE O NÚMERO-------------------------')
computador = randint(0,5)
num = int(input('Escolha um número entre 0 e 5: '))
print ('Processando...')
sleep(2)
if  computador == num:
    print ('Parabéns, você acertou!')
else: 
    print(f'Você errou!, o número pensado era {computador} e não {num}')
    print ('--------------------FIM DE JOGO----------------------')

   



        