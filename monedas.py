def convertir_moneda(moneda, moneda1):
    moneda1 = moneda1.upper()  # Convertir a mayúsculas para evitar problemas de comparación
    if moneda1 == "EUR":
        resultado = moneda * 0.93
        mensaje = f"El resultado es: {resultado} EUR"
    elif moneda1 == "ARS":
        resultado = moneda * 1150
        mensaje = f"El resultado es: {resultado} ARS"
    elif moneda1 == "BRL":
        resultado = moneda * 5.20
        mensaje = f"Es: {resultado} BRL"
    else:
        mensaje = "Moneda no válida"
    guardar_historial(moneda, moneda1, mensaje)
    return mensaje

# Definición de la función para guardar el historial de conversiones
def guardar_historial(moneda, moneda1, mensaje):
    with open("historial_conversiones.txt", "a") as archivo:
        archivo.write(f"Cantidad: {moneda}, Moneda: {moneda1}, Resultado: {mensaje}\n")

# Llamada a la función
try:
    moneda = float(input("Ingrese la cantidad de dinero a convertir (Por defecto está en USD): "))
    moneda1 = input("Ingrese la moneda a convertir (EUR/ARS/BRL): ").lower()
    mensaje = convertir_moneda(moneda, moneda1)
    print(mensaje)
    if "no válida" in mensaje:
        print("Conversión fallida. Moneda no válida.")
    else:
        print("Conversión exitosa.")
except ValueError:
    print("Error: Por favor, ingrese un número válido para la cantidad de dinero.")