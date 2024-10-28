print('=-'*15)
print('PROGRAMA TABUADA')
print('=-'*15)
from time import sleep
import os
while True:
    tabuada = int(input('Tabuada de qual valor? '))
    os.system('clear')
    if tabuada <0:
        sleep(1)
        print('Programa tabuada encerrado!')
        break
    for i in range(1,11):
        print(f'{tabuada} X {i} = {tabuada*i}')
        
        
   
