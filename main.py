# Solicitar al usuario que ingrese el dividendo y el divisor
dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))

# Realizar la división
cociente = dividendo // divisor
resto = dividendo % divisor

# Determinar si la división es exacta
if resto == 0:
    print("La división es exacta.")
    print(f"Cociente: {cociente}")
    print(f"Resto: {resto}")
else:
    print("La división no es exacta.")
    print(f"Cociente: {cociente}")
    print(f"Resto: {resto}")