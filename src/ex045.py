print ('-----------JOKENPÔ------------')
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint (0, 2) #computador escolhe 0,1 ou 2

print ('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA\n''')

jogador = int(input('Qual é a sua jogada? ')) #Jogador escolhe 0,1 ou 2

print ('\nJO')
sleep(1)
print ('KEN')
sleep(1)
print ('PO!!!\n')
sleep(1)
print ('=-'*14)
#Comparações para saber quem venceu
if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print ('EMPATE')
    elif jogador == 1:
        print ('JOGADOR VENCEU!')
    elif jogador == 2:
        print ('COMPUTADOR VENCEU!')
    else:
        print ('jOGADA INVÁLIDA!')
    
elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU!')
    else:
        print ('jOGADA INVÁLIDA!')
    
elif computador == 2:#computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCEU!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print ('jOGADA INVÁLIDA!')
        
print ('=-'*14)
print (f'O computador escolheu {itens[computador]}') #mostra o que o computador escolheu de acordo com o indice da variavel itens
print (f'O jogador jogou {itens[jogador]}') #mostra o que o jogador escolheu de acordo com o indice da variável itens










