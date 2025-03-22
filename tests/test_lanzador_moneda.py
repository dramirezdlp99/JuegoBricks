# tests/test_lanzador_moneda.py
from src.lanzador_moneda import lanzar_moneda

def test_lanzar_moneda():
    resultado = lanzar_moneda()
    assert resultado in ["Cara", "Cruz"]