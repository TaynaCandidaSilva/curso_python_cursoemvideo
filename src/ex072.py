numero_extenso = ('zero','um','dois', 'três','quatro', 
                  'cinco', 'seis', 'sete', 'oito', 'nove', 
                  'dez', 'onze', 'doze', 'treze', 'quatorze', 
                  'quinze', 'desseseis', 'dessesete', 'dezoito',
                  'dezenove', 'vinte')
numero = int(input('Digite um número em 0 e 20: '))
while numero  <0 or numero >20:
    numero = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {numero_extenso[numero]}')
