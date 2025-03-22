# src/simulador_clima.py
import random

def simular_clima(ciudad):
    """Simula el clima de una ciudad."""
    condiciones = ["soleado", "nublado", "lluvioso", "nevado", "tormentoso"]
    temperaturas = {
        "soleado": random.randint(20, 35),
        "nublado": random.randint(15, 25),
        "lluvioso": random.randint(10, 20),
        "nevado": random.randint(-5, 5),
        "tormentoso": random.randint(15, 30)
    }

    condicion = random.choice(condiciones)
    temperatura = temperaturas[condicion]

    return f"El clima en {ciudad} es {condicion} con una temperatura de {temperatura}°C."