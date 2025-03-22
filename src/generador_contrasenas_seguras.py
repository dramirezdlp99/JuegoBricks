# src/generador_contrasenas_seguras.py
import random
import string

def generar_contrasena(longitud):
    """Genera una contrasena segura."""
    # Definir los conjuntos de caracteres
    letras_minusculas = string.ascii_lowercase
    letras_mayusculas = string.ascii_uppercase
    digitos = string.digits
    caracteres_especiales = string.punctuation

    # Asegurarse de que la contraseña tenga al menos un carácter de cada tipo
    contrasena = [
        random.choice(letras_minusculas),
        random.choice(letras_mayusculas),
        random.choice(digitos),
        random.choice(caracteres_especiales)
    ]

    # Completar el resto de la contraseña con caracteres aleatorios
    todos_caracteres = letras_minusculas + letras_mayusculas + digitos + caracteres_especiales
    contrasena += [random.choice(todos_caracteres) for _ in range(longitud - 4)]

    # Mezclar la contraseña para que no esté en un orden predecible
    random.shuffle(contrasena)

    # Convertir la lista en una cadena
    return ''.join(contrasena)