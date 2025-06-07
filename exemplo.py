attributes = "Exemplo"
Titular = "Zé do pão com ovo"
PIN = 1925

AtributosValidos = ["Exemplo", "Deficiente"]
TitularesValidos = ["Zé do pão com ovo", "José", "Zé"]

def conta_bancaria():
    if attributes != "" and Titular != "":
        print("possivelmente valido, hora de validar PIN")
        if attributes == AtributosValidos[0] or AtributosValidos[1] and Titular == TitularesValidos[0] or TitularesValidos[1] or TitularesValidos[2]:
            print("Titular e Atributo validos.")
            checkpin = int(input("Digite seu PIN: "))
            if TypeError:
                print("ERRO: tentando debugar né seu retardado")
            else:
                if checkpin == PIN:
                    print("PIN valido, continue por favor.")
                else:
                    print("PIN Invalido.")
        else:
            print("Titular ou Atributo Invalido.")
    else:
        print("Por favor insira attributos.")

conta_bancaria()

