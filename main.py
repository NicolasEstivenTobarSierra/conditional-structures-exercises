# Solicitar al usuario que ingrese dos números
numero1 = int(input("Ingrese número: "))
numero2 = int(input("Ingrese número: "))

# Ordenar y mostrar los números
if numero1 < numero2:
    print(numero1, numero2)
else:
    print(numero2, numero1)