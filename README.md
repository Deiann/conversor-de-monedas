#  Conversor de Monedas en Python

Este proyecto es un conversor de divisas simple en Python que permite convertir montos desde USD a otras monedas (EUR, ARS, BRL) usando tasas de cambio fijas. También guarda un historial de conversiones en un archivo de texto.

---

## Descripción del Proyecto

El conversor solicita al usuario:

1. Una **cantidad en USD**.
2. Una **moneda destino**: EUR (euros), ARS (pesos argentinos), BRL (reales brasileños).

Después de la conversión, el resultado se muestra en pantalla y se guarda automáticamente en el archivo `historial_conversiones.txt`.

---

## 💹 Tasas de Cambio Utilizadas

| Moneda Destino | Tasa de Conversión desde USD |
|----------------|------------------------------|
| EUR            | 0.93                         |
| ARS            | 1150                         |
| BRL            | 5.20                         |

> ⚠️ Las tasas son valores fijos definidos dentro del código y no se actualizan automáticamente.

---

## 🧪 Ejemplo de Uso

**Entrada del usuario:Cantidad: 500.0, Moneda: EUR, Resultado: El resultado es: 465.0 EUR**
