# Solicitar al usuario que ingrese cuatro números
numero1 = int(input("Ingrese número: "))
numero2 = int(input("Ingrese número: "))
numero3 = int(input("Ingrese número: "))
numero4 = int(input("Ingrese número: "))

# Ordenar y mostrar los números
if numero1 <= numero2 and numero1 <= numero3 and numero1 <= numero4:
    if numero2 <= numero3 and numero2 <= numero4:
        if numero3 <= numero4:
            print(numero1, numero2, numero3, numero4)
        else:
            print(numero1, numero2, numero4, numero3)
    elif numero3 <= numero2 and numero3 <= numero4:
        if numero2 <= numero4:
            print(numero1, numero3, numero2, numero4)
        else:
            print(numero1, numero3, numero4, numero2)
    else:
        if numero2 <= numero3:
            print(numero1, numero4, numero2, numero3)
        else:
            print(numero1, numero4, numero3, numero2)
elif numero2 <= numero1 and numero2 <= numero3 and numero2 <= numero4:
    if numero1 <= numero3 and numero1 <= numero4:
        if numero3 <= numero4:
            print(numero2, numero1, numero3, numero4)
        else:
            print(numero2, numero1, numero4, numero3)
    elif numero3 <= numero1 and numero3 <= numero4:
        if numero1 <= numero4:
            print(numero2, numero3, numero1, numero4)
        else:
            print(numero2, numero3, numero4, numero1)
    else:
        if numero1 <= numero3:
            print(numero2, numero4, numero1, numero3)
        else:
            print(numero2, numero4, numero3, numero1)
elif numero3 <= numero1 and numero3 <= numero2 and numero3 <= numero4:
    if numero1 <= numero2 and numero1 <= numero4:
        if numero2 <= numero4:
            print(numero3, numero1, numero2, numero4)
        else:
            print(numero3, numero1, numero4, numero2)
    elif numero2 <= numero1 and numero2 <= numero4:
        if numero1 <= numero4:
            print(numero3, numero2, numero1, numero4)
        else:
            print(numero3, numero2, numero4, numero1)
    else:
        if numero1 <= numero2:
            print(numero3, numero4, numero1, numero2)
        else:
            print(numero3, numero4, numero2, numero1)
else:  # numero4 es el más pequeño
    if numero1 <= numero2 and numero1 <= numero3:
        if numero2 <= numero3:
            print(numero4, numero1, numero2, numero3)
        else:
            print(numero4, numero1, numero3, numero2)
    elif numero2 <= numero1 and numero2 <= numero3:
        if numero1 <= numero3:
            print(numero4, numero2, numero1, numero3)
        else:
            print(numero4, numero2, numero3, numero1)
    else:
        if numero1 <= numero2:
            print(numero4, numero3, numero1, numero2)
        else:
            print(numero4, numero3, numero2, numero1)