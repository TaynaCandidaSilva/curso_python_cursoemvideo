from random import randint
from time import sleep


def sorteia(lista):
    print("Sorteando 5 valores da lista: ", end="")
    for n in range(0, 5):
        numeros = randint(1, 10)
        lista.append(numeros)
        print(f"{numeros} ", end="", flush=True)
        sleep(0.3)
    print(f"Pronto!")


def soma_par(lista):
    total = 0
    for n in lista:
        if n % 2 == 0:
            total += n
    print(f"Somando os números sorteados {lista}, temos {total}")


numeros = list()
sorteia(numeros)
soma_par(numeros)
