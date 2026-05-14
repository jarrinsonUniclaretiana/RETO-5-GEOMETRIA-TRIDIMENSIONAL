"""
Módulo: cilindro.py
Integrante A - Reto 5: Geometría Tridimensional
UNICLARETIANA - Taller de Programación Modular en Python

Descripción:
    Módulo para calcular el volumen y el área superficial de un Cilindro.
    
Fórmulas utilizadas:
    - Volumen      : V = π * r² * h
    - Área Total   : A = 2 * π * r * (r + h)
"""

import math


def calcular_volumen(radio, altura):
    """
    Calcula el volumen de un cilindro.

    Parámetros:
        radio  (float): Radio de la base del cilindro (en cualquier unidad).
        altura (float): Altura del cilindro (misma unidad que el radio).

    Retorna:
        float: Volumen del cilindro.
    
    Ejemplo:
        >>> calcular_volumen(3, 5)
        141.3716694115407
    """
    if radio <= 0 or altura <= 0:
        raise ValueError("El radio y la altura deben ser valores positivos.")
    
    volumen = math.pi * radio ** 2 * altura
    return round(volumen, 4)


def calcular_area_superficial(radio, altura):
    """
    Calcula el área superficial total de un cilindro.
    Incluye las dos bases circulares y la superficie lateral.

    Parámetros:
        radio  (float): Radio de la base del cilindro.
        altura (float): Altura del cilindro.

    Retorna:
        float: Área superficial total del cilindro.
    
    Ejemplo:
        >>> calcular_area_superficial(3, 5)
        150.7964473723100
    """
    if radio <= 0 or altura <= 0:
        raise ValueError("El radio y la altura deben ser valores positivos.")
    
    area = 2 * math.pi * radio * (radio + altura)
    return round(area, 4)


def mostrar_resultados(radio, altura):
    """
    Muestra en consola el volumen y el área superficial del cilindro
    con los datos ingresados.

    Parámetros:
        radio  (float): Radio de la base del cilindro.
        altura (float): Altura del cilindro.
    """
    volumen = calcular_volumen(radio, altura)
    area    = calcular_area_superficial(radio, altura)

    print("=" * 45)
    print("       CÁLCULO - CILINDRO")
    print("=" * 45)
    print(f"  Radio            : {radio} unidades")
    print(f"  Altura           : {altura} unidades")
    print("-" * 45)
    print(f"  Volumen          : {volumen} unidades³")
    print(f"  Área Superficial : {area} unidades²")
    print("=" * 45)


# Ejecución directa del módulo (para pruebas individuales)
if __name__ == "__main__":
    print("--- Prueba del módulo cilindro.py ---\n")
    
    radio  = float(input("Ingrese el radio del cilindro  : "))
    altura = float(input("Ingrese la altura del cilindro : "))
    
    mostrar_resultados(radio, altura)
