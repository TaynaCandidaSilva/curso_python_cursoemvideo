nome = str (input('Digite o seu nome completo: ')).strip()
print (f'seu nome em maiúscolo é {nome.upper()}')
print (f'seu nome em minúculo é {nome.lower()}')
separa = nome.split()
print (f'seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')