def validateStringInput(input:str) -> bool:
    try:
        validation = False
        input = input.strip()
        if len(input) > 0:
            if not input.isalpha():
                raise ValueError("Valor invalido!")
            else:
                validation = True
        else:
            raise ValueError("O valor não pode ser vazio!")
        return validation
    except Exception as e:
        print(e)

def validateExit(confirm:str) -> bool:
    try:
        validation = False
        confirm = confirm.strip()
        if len(confirm) > 0:
            validation = True if confirm.isalpha() and confirm.islower() == "sim" else False
            if not validation:
                raise ValueError("Valor invalido!")
        else:
            raise ValueError("O valor não pode ser vazio!")
        return validation
    except Exception as e:
        print(e)