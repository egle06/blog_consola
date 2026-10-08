"""
menu.py

Interacción con el usuario: muestra el menú y pide datos por consola.
"""

from blog.datos import estados_post


def mostrar_menu():
    """
    Muestra el menú principal y captura la opción elegida.
    Retorna la opción como entero, o None si la entrada no fue válida.
    """
    print("\n--- MENÚ DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por título")
    print("3. Filtrar por tag")
    print("4. Crear nuevo post")
    print("5. Validar posts")
    print("6. Guardar posts en JSON")
    print("7. Salir")

    entrada = input("\nElegí una opción (1-7): ")

    try:
        return int(entrada)
    except ValueError:
        print("\nEntrada inválida: debés ingresar un número.")
        return None


def pedir_datos_nuevo_post():
    """
    Pide por consola los datos de un nuevo post.
    Retorna (titulo, contenido, tags, estado). Los tags se separan por comas.
    La validación de campos vacíos la hace Blog.crear_post().
    """
    print("\n--- NUEVO POST ---")
    titulo = input("Título: ")
    contenido = input("Contenido: ")
    tags = input("Tags (separados por coma): ").split(",")
    estado = input(f"Estado ({', '.join(estados_post)}): ")
    return titulo, contenido, tags, estado