a = int(input('Informe o 1° número:  '))
b = int(input('Informe o 2° número:  '))
c = int(input('Informe o 3° número:  '))
#Verificando o menor valor
menor = a #Começo determinando o a como menor
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c 

#Verificando o maior valor       
maior = a #Começo determinando o a como maior
if  b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
    
print (f'O menor valor é {menor}')
print (f'O maior valor é {maior}')

