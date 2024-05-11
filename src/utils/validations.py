def validateStringInput(input:str) -> bool:
    try:
        if len(input) > 0:
            if not input.strip().isalpha():
                raise ValueError("Valor invalido!")
        else:
            raise ValueError("O valor não pode ser vazio!")
    except Exception as e:
        print(e)

def validateExit(confirm:str) -> bool:
    try:
        validation = False
        if len(confirm) > 0:
            validation = True if confirm.strip().isalpha() and confirm.strip().islower() == "sim" else False
            if not validation:
                raise ValueError("Valor invalido!")
        else:
            raise ValueError("O valor não pode ser vazio!")
        return validation
    except Exception as e:
        print(e)