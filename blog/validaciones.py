"""
validaciones.py

Reglas lógicas del sistema: verifica que un objeto Post tenga datos correctos.
"""

from blog.datos import estados_post
from blog.modelos import Autor, Post


def validar_post(post):
    """
    Verifica que un Post cumpla con las reglas esperadas.
    Retorna una tupla (es_valido, mensaje):
        - es_valido: True o False
        - mensaje: "OK" si es válido, o una descripción del error encontrado
    """
    # 1. Debe ser un objeto Post
    if not isinstance(post, Post):
        return False, "no es un objeto Post"

    # 2. El id debe ser un entero
    if not isinstance(post.id, int):
        return False, "el id no es un número entero"

    # 3. El título no debe estar vacío
    if not isinstance(post.titulo, str) or post.titulo.strip() == "":
        return False, "el título está vacío o no es texto"

    # 4. El contenido no debe estar vacío
    if not isinstance(post.contenido, str) or post.contenido.strip() == "":
        return False, "el contenido está vacío o no es texto"

    # 5. El autor debe ser un objeto Autor con nombre
    if not isinstance(post.autor, Autor):
        return False, "el autor no es un objeto Autor"
    if not isinstance(post.autor.nombre, str) or post.autor.nombre.strip() == "":
        return False, "el autor no tiene nombre"

    # 6. Tags debe ser una lista de textos
    if not isinstance(post.tags, list):
        return False, "tags no es una lista"
    if not all(isinstance(t, str) for t in post.tags):
        return False, "todos los tags deben ser texto"

    # 7. El estado debe pertenecer a estados_post
    if post.estado not in estados_post:
        return False, f'el estado "{post.estado}" no es válido'

    return True, "OK"