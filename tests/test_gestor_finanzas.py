# tests/test_gestor_finanzas.py
from src.gestor_finanzas import GestorFinanzas

def test_gestor_finanzas():
    gestor = GestorFinanzas()
    gestor.agregar_ingreso(1000, "Salario")
    gestor.agregar_gasto(200, "Comida")
    assert gestor.calcular_balance() == 800
    assert len(gestor.transacciones) == 2