# tests/test_generador_contrasenas_seguras.py
from src.generador_contrasenas_seguras import generar_contrasena

def test_generar_contrasena():
    contrasena = generar_contrasena(12)
    assert len(contrasena) == 12
    assert any(c in contrasena for c in "abcdefghijklmnopqrstuvwxyz")  # Letras minúsculas
    assert any(c in contrasena for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ")  # Letras mayúsculas
    assert any(c in contrasena for c in "0123456789")  # Dígitos
    assert any(c in contrasena for c in "!@#$%^&*()_+")  # Caracteres especiales