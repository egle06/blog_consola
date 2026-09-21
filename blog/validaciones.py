"""
validaciones.py

Reglas lógicas del sistema: verifica que un post tenga la estructura esperada.
"""

from blog.datos import estados_post


def validar_post(post):
    """
    Verifica que un post cumpla con la estructura esperada.
    Retorna una tupla (es_valido, mensaje):
        - es_valido: True o False
        - mensaje: "OK" si es válido, o una descripción del error encontrado
    """
    claves_obligatorias = ["id", "titulo", "contenido", "autor", "tags", "estado"]

    # 1. El post debe ser un diccionario
    if not isinstance(post, dict):
        return False, "el post no es un diccionario"

    # 2. Deben existir todas las claves obligatorias
    for clave in claves_obligatorias:
        if clave not in post:
            return False, f'falta la clave "{clave}"'

    # 3. El título no debe estar vacío
    if not isinstance(post["titulo"], str) or post["titulo"].strip() == "":
        return False, "el título está vacío o no es texto"

    # 4. El contenido no debe estar vacío
    if not isinstance(post["contenido"], str) or post["contenido"].strip() == "":
        return False, "el contenido está vacío o no es texto"

    # 5. El autor debe ser un diccionario
    if not isinstance(post["autor"], dict):
        return False, "el autor no es un diccionario"

    # 6. El autor debe tener la clave "nombre"
    if "nombre" not in post["autor"]:
        return False, 'el autor no tiene la clave "nombre"'

    # 7. Tags debe ser una lista
    if not isinstance(post["tags"], list):
        return False, "tags no es una lista"

    # 8. El estado debe pertenecer a estados_post
    if post["estado"] not in estados_post:
        return False, f'el estado "{post["estado"]}" no es válido'

    return True, "OK"