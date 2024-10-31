# Solicitar al usuario que ingrese el primer operando
operando1 = float(input("Operando: "))
# Solicitar al usuario que ingrese el operador
operador = input("Operador: ")
# Solicitar al usuario que ingrese el segundo operando
operando2 = float(input("Operando: "))

# Realizar la operación según el operador ingresado
if operador == '+':
    resultado = operando1 + operando2
    print(f"{operando1} + {operando2} = {resultado}")
elif operador == '-':
    resultado = operando1 - operando2
    print(f"{operando1} - {operando2} = {resultado}")
elif operador == '*':
    resultado = operando1 * operando2
    print(f"{operando1} * {operando2} = {resultado}")
elif operador == '/':
    if operando2 != 0:
        resultado = operando1 / operando2
        print(f"{operando1} / {operando2} = {resultado}")
    else:
        print("Error: División por cero.")
elif operador == '**':
    resultado = operando1 ** operando2
    print(f"{operando1} ** {operando2} = {resultado}")
else:
    print("Error: Operador no válido.")