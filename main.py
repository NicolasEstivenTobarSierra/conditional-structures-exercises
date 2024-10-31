# Solicitar al usuario que ingrese los tres lados del triángulo
a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))

# Verificar si los lados forman un triángulo válido
if a + b > c and a + c > b and b + c > a:
    # Determinar el tipo de triángulo
    if a == b == c:
        print("El triángulo es equilátero.")
    elif a == b or a == c or b == c:
        print("El triángulo es isósceles.")
    else:
        print("El triángulo es escaleno.")
else:
    print("No es un triángulo válido.")