"""
menu.py

Interacción con el usuario: muestra el menú y captura la opción elegida.
"""


def mostrar_menu():
    """
    Muestra el menú principal y captura la opción elegida por el usuario.
    Usa try-except para evitar que el programa se cierre si se ingresa
    un valor no numérico. Retorna la opción como número entero, o None
    si la entrada no fue válida.
    """
    print("\n--- MENÚ DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por título")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")

    entrada = input("\nElegí una opción (1-5): ")

    try:
        opcion = int(entrada)
        return opcion
    except ValueError:
        # El usuario ingresó texto en lugar de un número
        print("\nEntrada inválida: debés ingresar un número.")
        return None