from datetime import datetime

trabalhador = dict()
trabalhador["nome"] = input("Nome: ")
nasc = int(input("Ano de nascimento: "))
trabalhador["idade"] = datetime.now().year - nasc
trabalhador["CTPS"] = int(input("Carteira de Trabalho (0 não tem): "))
if trabalhador["CTPS"] != 0:
    trabalhador["contratacao"] = int(input("Ano de contratação: "))
    trabalhador["salario"] = float(input("Salário: "))
    trabalhador["aposentaria"] = trabalhador["idade"] + (
        (trabalhador["contratacao"] + 35) - datetime.now().year
    )
for k, v in trabalhador.items():
    print(f"    - {k} tem o valor {v}")
