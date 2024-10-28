def maior(*numeros):
    cont = maior = 0
    print("-=" * 30)
    print(f"Analisando os valores passados... ")
    for valor in numeros:
        print(f"{valor} ", end="", flush=True)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f"Foram informados {cont} valores ao todo.")
    print(f"O maior valor informado foi {maior}")


maior(1, 5, 3)
maior(3, 2)
maior(8, 9, 7)
maior(0)
maior(5)
