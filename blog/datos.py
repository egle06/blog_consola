"""
datos.py

Datos de referencia del blog y persistencia en JSON:
- Carga de posts desde posts.json (diccionarios -> objetos Post).
- Guardado de posts en posts.json (objetos -> diccionarios).
"""

import json
from pathlib import Path

from blog.modelos import crear_post_desde_dict

# posts.json queda en la raíz del proyecto, sin importar desde dónde se ejecute
RUTA_POSTS = Path(__file__).resolve().parent.parent / "posts.json"

perfil_autor = {
    "nombre": "Egle Aldana Martinelli",
    "bio": "Estudiante de Data Science y especialista en calidad.",
    "especialidad": "Data Science y Python",
    "redes_sociales": ["@egle_data", "@egle_python"]
}

estados_post = ("borrador", "publicado", "archivado")

etiquetas_blog = {"Data Science", "Python", "Calidad", "Logística"}


def cargar_posts(ruta=RUTA_POSTS):
    """
    Lee posts.json y retorna una lista de objetos Post.
    Nunca cierra el programa: si hay un problema, informa y retorna
    lo que se pudo cargar (o una lista vacía).
    """
    ruta = Path(ruta)

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
    except FileNotFoundError:
        print(f"Aviso: no existe {ruta.name}. Se inicia con un blog vacío "
              f"(se creará al guardar).")
        return []
    except OSError as error:
        print(f"Error al leer {ruta.name}: {error}. Se inicia con un blog vacío.")
        return []

    if contenido.strip() == "":
        print(f"Aviso: {ruta.name} está vacío. Se inicia con un blog vacío.")
        return []

    try:
        datos = json.loads(contenido)
    except json.JSONDecodeError as error:
        print(f"Error: {ruta.name} tiene contenido JSON inválido ({error}). "
              f"Se inicia con un blog vacío.")
        return []

    if not isinstance(datos, list):
        print(f"Error: {ruta.name} debe contener una lista de posts. "
              f"Se inicia con un blog vacío.")
        return []

    posts = []
    for posicion, item in enumerate(datos, start=1):
        try:
            posts.append(crear_post_desde_dict(item))
        except (ValueError, TypeError) as error:
            print(f"Aviso: se omitió el elemento {posicion} de {ruta.name}: {error}.")

    return posts


def guardar_posts(lista_de_dicts, ruta=RUTA_POSTS):
    """
    Guarda en JSON una lista de diccionarios (usar blog.to_list()).
    Retorna True si se guardó bien, False si hubo un error.
    """
    if not isinstance(lista_de_dicts, list) or not all(
        isinstance(item, dict) for item in lista_de_dicts
    ):
        print("Error: los posts deben convertirse a diccionarios antes de "
              "guardarse (usá blog.to_list()).")
        return False

    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(lista_de_dicts, archivo, ensure_ascii=False, indent=4)
    except (OSError, TypeError) as error:
        print(f"Error al guardar en {Path(ruta).name}: {error}")
        return False

    return True