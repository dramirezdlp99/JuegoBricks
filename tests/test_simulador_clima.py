# tests/test_simulador_clima.py
from src.simulador_clima import simular_clima

def test_simular_clima():
    clima = simular_clima("Bogotá")
    assert "Bogotá" in clima
    assert any(condicion in clima for condicion in ["soleado", "nublado", "lluvioso", "nevado", "tormentoso"])