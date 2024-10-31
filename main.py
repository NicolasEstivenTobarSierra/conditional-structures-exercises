# Solicitar al usuario que ingrese su estatura, peso y edad
estatura = float(input("Ingrese su estatura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))
edad = int(input("Ingrese su edad: "))

# Calcular el índice de masa corporal (IMC)
imc = peso / (estatura ** 2)

# Determinar la condición de riesgo
if edad < 45:
    if imc < 22.0:
        riesgo = "bajo"
    else:
        riesgo = "medio"
else:
    if imc < 22.0:
        riesgo = "medio"
    else:
        riesgo = "alto"

# Mostrar el resultado
print(f"Su IMC es: {imc:.2f}")
print(f"Condición de riesgo: {riesgo}")