# src/gestor_finanzas.py

class GestorFinanzas:
    def __init__(self):
        self.transacciones = []

    def agregar_ingreso(self, monto, descripcion):
        """Agrega un ingreso."""
        self.transacciones.append({"tipo": "ingreso", "monto": monto, "descripcion": descripcion})

    def agregar_gasto(self, monto, descripcion):
        """Agrega un gasto."""
        self.transacciones.append({"tipo": "gasto", "monto": monto, "descripcion": descripcion})

    def calcular_balance(self):
        """Calcula el balance total."""
        ingresos = sum(t["monto"] for t in self.transacciones if t["tipo"] == "ingreso")
        gastos = sum(t["monto"] for t in self.transacciones if t["tipo"] == "gasto")
        return ingresos - gastos

    def mostrar_transacciones(self):
        """Muestra todas las transacciones."""
        return "\n".join(f"{t['tipo'].capitalize()}: ${t['monto']} ({t['descripcion']})" for t in self.transacciones)