"""
operaciones.py

Funciones principales del blog: listar, buscar por título y filtrar por tag.
Todas reciben los datos por parámetro (no dependen de variables globales).
"""


def listar_posts(lista):
    """
    Recorre la lista de posts y muestra título, autor y estado de cada uno.
    Usa .get() para evitar errores si a algún post le faltan claves.
    """
    if not lista:
        print("\nNo hay posts para mostrar.")
        return

    print("\nPosts disponibles:")
    for post in lista:
        titulo = post.get("titulo", "(sin título)")
        estado = post.get("estado", "(sin estado)")

        # El autor puede no ser un diccionario en posts con datos incorrectos
        autor = post.get("autor")
        if isinstance(autor, dict):
            nombre_autor = autor.get("nombre", "(autor sin nombre)")
        else:
            nombre_autor = "(autor con formato inválido)"

        print(f"- {titulo} | Autor: {nombre_autor} | Estado: {estado}")


def buscar_por_titulo(lista, termino):
    """
    Recibe la lista de posts y un término de búsqueda.
    Retorna una lista con los posts cuyo título contiene el término,
    ignorando mayúsculas y minúsculas.
    """
    resultados = []
    termino = termino.lower()

    for post in lista:
        titulo = post.get("titulo", "")
        # Solo comparamos si el título es un string válido
        if isinstance(titulo, str) and termino in titulo.lower():
            resultados.append(post)

    return resultados


def filtrar_por_tag(lista, tag):
    """
    Recibe la lista de posts y un tag a buscar.
    Retorna una lista con los posts que tengan ese tag,
    ignorando mayúsculas y minúsculas.
    """
    resultados = []
    tag_buscado = tag.lower()

    for post in lista:
        tags_post = post.get("tags", [])

        # Nos protegemos por si "tags" no es una lista (post inválido)
        if not isinstance(tags_post, list):
            continue

        for t in tags_post:
            if isinstance(t, str) and t.lower() == tag_buscado:
                resultados.append(post)
                break  # Evita agregar el mismo post dos veces

    return resultados