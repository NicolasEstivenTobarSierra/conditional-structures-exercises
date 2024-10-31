# Solicitar al usuario que ingrese un año
año = int(input("Ingrese un año: "))

# Determinar si el año es bisiesto
if año < 1582:
    # Regla del calendario juliano
    if año % 4 == 0:
        print(f"{año} es bisiesto")
    else:
        print(f"{año} no es bisiesto")
else:
    # Regla del calendario gregoriano
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        print(f"{año} es bisiesto")
    else:
        print(f"{año} no es bisiesto")