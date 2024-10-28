classificacao = ('Botafogo','Palmeiras', 'Grêmio', 'Flamengo',
                 'Fluminense', 'Bragantino','Athletico-PR','Fortaleza',
                 'Atlético-MG', 'Cuiabá','São Paulo', 'Cruzeiro',
                 'Corinthians', 'Internacional','Goiás','Bahia',	
                 'Santos', 'Vasco', 'América-MG','Coritiba')
    
print(f'Os 5 primeiros colocados são: {classificacao[0:5]}')
print()
print(f'O últimos 4 colocados da tabela são: {classificacao[-4:]}')
print()
print(f'Times em ordem Alfabética: {sorted(classificacao)}')
print()
print(f'O time do São Paulo está posição: {classificacao.index("São Paulo")+1}ª posição')