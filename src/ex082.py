#Inicializando as variáveis
lista = []
lista_impares = []
lista_pares = []

#Alimentando a lista com vários números aleatórios
while True:
    lista.append (int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
#Análisando os números

for i,v in enumerate(lista):
    if v % 2 == 0:
        lista_pares.append(v)
    else:
        lista_impares.append(v)
    
#Printando as listas
print(f'A lista de valores é {lista}')
print(f'A lista de pares é {lista_pares}')
print(f'A lista de impares é {lista_impares}')