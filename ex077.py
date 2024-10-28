palavras = ('aprender', 'programar', 'linguagem',
            'curso', 'gratis', 'estudar')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')