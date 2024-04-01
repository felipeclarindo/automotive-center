import requests
import json

url = "http://127.0.0.1:5000"

while True:
    print("""
Centro Automotivo Porto
1 - Busca de problemas comums
2 - Busca de carros com mais problema
3 - Busca de orçamento para problemas
    """)
    choice = int(input("Informe a opção desejada: "))

    match choice:
        case 1:
            try:
                carro = input("Digite o carro cujo quer buscar problemas comums: ").title()
                problemas = requests.get("http://127.0.0.1:5000/cars-problems").json()
                problema = problemas.get(carro)
                if problema:
                    print(f"Carro: {carro}")
                    print(f"Problema: {problema}")
                else:
                    print("Carro não encontrado.")
            except Exception as e:
                print(f"Ocorreu um erro ao buscar problemas comums: {e}")
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case _:
            break