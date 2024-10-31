# Función para determinar el estado del set
def estado_set(juegos_a, juegos_b):
    # Verificar condiciones de resultado inválido
    if (juegos_a >= 7 and juegos_b >= 6) or (juegos_b >= 7 and juegos_a >= 6) or (juegos_a > 6 and juegos_b > 6 and abs(juegos_a - juegos_b) < 2):
        return "Invalido"

    # Verificar si A ha ganado
    if juegos_a >= 6 and juegos_a - juegos_b >= 2:
        return "Gano A"
    
    # Verificar si B ha ganado
    if juegos_b >= 6 and juegos_b - juegos_a >= 2:
        return "Gano B"
    
    # Verificar si el set aún no ha terminado
    return "Aun no termina"

# Solicitar los juegos ganados por A y B
while True:
    juegos_a = int(input("Juegos ganados por A: "))
    juegos_b = int(input("Juegos ganados por B: "))
    
    resultado = estado_set(juegos_a, juegos_b)
    print(resultado)
