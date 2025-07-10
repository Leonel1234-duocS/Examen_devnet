import math

def calcular_circunferencia(radio):
    return 2 * math.pi * radio

# Cálculos para radios solicitados
radio_3 = calcular_circunferencia(3)
radio_8 = calcular_circunferencia(8)
radio_10 = calcular_circunferencia(10)

# Resultados en español
print(f"Circunferencia con radio 3: {radio_3:.2f}")  # :.2f redondea a 2 decimales
print(f"Circunferencia con radio 8: {radio_8:.2f}")
print(f"Circunferencia con radio 10: {radio_10:.2f}")
print("¡Todos los cálculos fueron completados exitosamente en español!")
