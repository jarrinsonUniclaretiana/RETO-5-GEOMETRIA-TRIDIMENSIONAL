"""
Módulo: esfera.py
Integrante B - Reto 5: Geometría Tridimensional
UNICLARETIANA - Taller de Programación Modular en Python

Fórmulas utilizadas:
    - Volumen      : V = (4/3) * π * r³
    - Área Total   : A = 4 * π * r²
"""

import math


def calcular_volumen(radio):
    """
    Calcula el volumen de una esfera.

    Parámetros:
        radio (float): Radio de la esfera.

    Retorna:
        float: Volumen de la esfera.
    """
    if radio <= 0:
        raise ValueError("El radio debe ser un valor positivo.")
    
    volumen = (4/3) * math.pi * radio ** 3
    return round(volumen, 4)


def calcular_area_superficial(radio):
    """
    Calcula el área superficial de una esfera.

    Parámetros:
        radio (float): Radio de la esfera.

    Retorna:
        float: Área superficial de la esfera.
    """
    if radio <= 0:
        raise ValueError("El radio debe ser un valor positivo.")
    
    area = 4 * math.pi * radio ** 2
    return round(area, 4)


def mostrar_resultados(radio):
    """
    Muestra en consola el volumen y el área superficial de la esfera.

    Parámetros:
        radio (float): Radio de la esfera.
    """
    volumen = calcular_volumen(radio)
    area    = calcular_area_superficial(radio)

    print("=" * 45)
    print("       CÁLCULO - ESFERA")
    print("=" * 45)
    print(f"  Radio            : {radio} unidades")
    print("-" * 45)
    print(f"  Volumen          : {volumen} unidades³")
    print(f"  Área Superficial : {area} unidades²")
    print("=" * 45)


if __name__ == "__main__":
    print("--- Prueba del módulo esfera.py ---\n")
    radio = float(input("Ingrese el radio de la esfera : "))
    mostrar_resultados(radio)
