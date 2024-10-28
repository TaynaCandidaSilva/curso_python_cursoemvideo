frase = str(input('Digite um frase: ')).upper().strip()
print ('a letra A aparece', frase.count('A'), 'vezes no texto digitado')
print ('a letra a aparece 1° vez na posição: ', frase.find('A')+1)
print ('a letra a aparece a ultima vezes na posição: ', frase.rfind('A')+1)
