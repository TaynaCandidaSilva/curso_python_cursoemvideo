frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}')
for letra in range(len(junto)-1,-1, -1):
    inverso += junto[letra]
if inverso == junto:
    print ('Temos um palíndromo!')
else:
    print ('A frase digiada não é um palíndromo!')