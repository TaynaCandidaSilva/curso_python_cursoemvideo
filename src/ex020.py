from random import shuffle
n1 = input('Aluno 1: ')
n2 = input ('Aluno 2: ')
n3 = input ('Aluno 3: ')
lista = [n1, n2, n3]
shuffle(lista)
print ('A ordem de apresentação será a seguinte: ')
print (lista)

