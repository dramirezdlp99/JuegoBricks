# src/lanzador_moneda.py
import random

def lanzar_moneda():
    """Simula el lanzamiento de una moneda."""
    resultado = random.choice(["Cara", "Cruz"])
    return resultado