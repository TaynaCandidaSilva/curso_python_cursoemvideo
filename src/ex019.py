from random import choice
aluno1 = input ('Primeiro aluno: ')
aluno2 = input ('Segundo aluno: ')
aluno3 = input ('Terceiro aluno: ')
aluno4 = input ('Quarto aluno: ')
list = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(list)
print (f'O aluno escolhido foi {escolhido}')






