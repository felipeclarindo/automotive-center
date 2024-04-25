from modules.utils import *
from time import sleep
from tabulate import tabulate

url = "http://127.0.0.1:5000"

while True:
    clear()
    try:
        print("""
Centro Automotivo Porto
1 - Buscar problemas comums
2 - Buscar orçamento
3 - Mostrar carros que costumam dar mais problemas
4 - Sair
        """)
        choice = int(input("Informe a opção desejada: "))
    
        match choice:
            case 1:
                try:
                    clear()
                    brend = input("Informe a marca de carro cujo deseja buscar problemas comums: ").title().strip()
                    clear()
                    print("Buscando...")
                    sleep(1)
                    clear()
                    problem = searchProblems(url, brend)
                    if problem:
                        print("Problema identificado!")
                        print(f"Marca: {brend}")
                        print(f"Problema: {problem}")
                except ValueError as e:
                    print(f"Erro de valor: {e}")
                except Exception as e:
                    print(f"Erro inesperado: {e}")
            case 2:
                try:
                    clear()
                    brend = input("Informe a marca para verificar orçamento: ").title().strip()
                    clear()
                    print("Buscando...")
                    sleep(1)
                    clear()
                    dados = searchPrice(url, brend)
                    tabela = tabulate(dados, headers="firstrow", tablefmt="grid")
                    print(tabela)
                except Exception as e:
                    print(f"Erro inesperado: {e}")
            case 3:
                try:
                    print("Buscando...")
                    sleep(1)
                    clear()
                    dados = showCarsMoreProblems(url)
                    tabela = tabulate(dados, headers="firstrow", tablefmt="grid")
                    print(tabela)
                except ValueError as e:
                    print(f"Erro de valor: {e}")
                except Exception as e: 
                    print(f"Erro inesperado: {e}")
            case 4:
                try:
                    clear()
                    confirm = str(input("Deseja mesmo sair? [Sim/Nao]")).title()[0].strip()
                    if confirm == "S":
                        clear()
                        print("Programa finalizado!")
                        break
                    elif confirm == "N":
                        clear()
                        continue
                    else:
                        raise ValueError("Valor invalido.")
                    
                except Exception as e:
                    print(f"Erro: {e}")
            case _:
                print("Opção ínvalida.")
                
    except ValueError as e:
        print(f"Erro de valor: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        input("Aperte ENTER para continuar")
        clear()