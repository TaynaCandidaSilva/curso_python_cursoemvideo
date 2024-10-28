print (f'---------------Calculando média de notas-------------------')
nota1 = float(input('Informe a 1° nota: '))
nota2 = float(input('Informe a 2° nota: '))
media = (nota1 + nota2) /2
print (f'Com as notas {nota1} e {nota2} a média do aluno é {media}')
if  media < 5:
    print('O aluno está REPROVADO!')
elif media >= 7:
    print ('O aluno está de APROVADO!')
else: 
    print ('O aluno está RECUPERAÇÃO!')