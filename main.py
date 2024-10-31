# Solicitar al usuario que ingrese un carácter
caracter = input("Ingrese carácter: ")

# Verificar si es un número
if caracter.isdigit():
    print("Es número.")
# Verificar si es una letra
elif caracter.isalpha():
    if caracter.isupper():
        print("Es letra mayúscula.")
    else:
        print("Es letra minúscula.")
# Si no es ni letra ni número
else:
    print("No es letra ni número.")