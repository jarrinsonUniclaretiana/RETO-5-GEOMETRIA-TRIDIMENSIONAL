"""
Archivo: main.py
Reto 5: Geometría Tridimensional
UNICLARETIANA - Taller de Programación Modular en Python

Descripción:
    Archivo principal que importa y ejecuta los tres módulos
    del equipo: cilindro, esfera y cono.
"""

# ── Importación de los tres módulos del equipo ──────────────────────────────
from cilindro import mostrar_resultados as resultados_cilindro
from esfera   import mostrar_resultados as resultados_esfera
from cono     import mostrar_resultados as resultados_cono


# ── Función principal ────────────────────────────────────────────────────────
def main():
    print("\n" + "=" * 50)
    print("   RETO 5 - GEOMETRÍA TRIDIMENSIONAL")
    print("   UNICLARETIANA - Programación Modular")
    print("=" * 50)

    # ── CILINDRO (Integrante A) ──────────────────────────────────────────────
    print("\n📦 CILINDRO")
    radio_c  = float(input("  Radio del cilindro  : "))
    altura_c = float(input("  Altura del cilindro : "))
    resultados_cilindro(radio_c, altura_c)

    # ── ESFERA (Integrante B) ────────────────────────────────────────────────
    print("\n🔵 ESFERA")
    radio_e = float(input("  Radio de la esfera  : "))
    resultados_esfera(radio_e)

    # ── CONO (Integrante C) ──────────────────────────────────────────────────
    print("\n🔺 CONO")
    radio_co  = float(input("  Radio de la base del cono : "))
    altura_co = float(input("  Altura del cono           : "))
    resultados_cono(radio_co, altura_co)

    print("\n✅ Programa finalizado correctamente.")
    print("=" * 50 + "\n")


# ── Punto de entrada ─────────────────────────────────────────────────────────
if __name__ == "__main__":
    main()
