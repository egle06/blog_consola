"""
modelos.py

Clases principales del sistema: Autor, Post y Blog.
Incluye también las funciones que reconstruyen objetos desde diccionarios
(necesarias para cargar los datos desde posts.json).

Este archivo no importa ningún otro módulo del proyecto.
"""


class Autor:
    """Persona que escribe los posts del blog."""

    def __init__(self, nombre, bio, especialidad, redes_sociales):
        self.nombre = nombre
        self.bio = bio
        self.especialidad = especialidad
        self.redes_sociales = redes_sociales

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "bio": self.bio,
            "especialidad": self.especialidad,
            "redes_sociales": self.redes_sociales
        }

    def __str__(self):
        return self.nombre


class Post:
    """Publicación del blog. Su autor es un objeto de la clase Autor."""

    def __init__(self, id, titulo, contenido, autor, tags, estado="borrador"):
        if not isinstance(autor, Autor):
            raise TypeError("el autor de un Post debe ser un objeto Autor")

        self.id = id
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor
        self.tags = tags
        self.estado = estado

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": self.autor.to_dict(),
            "tags": self.tags,
            "estado": self.estado
        }


class Blog:
    """Centraliza la lógica del sistema. Guarda una lista de objetos Post."""

    def __init__(self, posts=None):
        if posts is None:
            self.posts = []
        else:
            self.posts = posts

    def obtener_posts(self):
        return self.posts

    def listar_posts(self, posts=None):
        """
        Muestra título, autor y estado. Sin argumentos muestra todos los
        posts del blog; si se le pasa una lista, muestra esa lista
        (por ejemplo, el resultado de una búsqueda).
        """
        if posts is None:
            posts = self.posts

        if not posts:
            print("\nNo hay posts para mostrar.")
            return

        print("\nPosts disponibles:")
        for post in posts:
            print(f"- {post.titulo} | Autor: {post.autor.nombre} | Estado: {post.estado}")

    def buscar_por_titulo(self, termino):
        """Retorna los posts cuyo título contiene el término (ignora mayúsculas)."""
        resultados = []
        termino = termino.lower()

        for post in self.posts:
            if isinstance(post.titulo, str) and termino in post.titulo.lower():
                resultados.append(post)

        return resultados

    def filtrar_por_tag(self, tag):
        """Retorna los posts que tienen el tag (ignora mayúsculas)."""
        resultados = []
        tag = tag.lower()

        for post in self.posts:
            if not isinstance(post.tags, list):
                continue

            for t in post.tags:
                if isinstance(t, str) and t.lower() == tag:
                    resultados.append(post)
                    break

        return resultados

    def _siguiente_id(self):
        """Calcula el id del próximo post: el mayor id actual + 1."""
        mayor = 0
        for post in self.posts:
            if isinstance(post.id, int) and post.id > mayor:
                mayor = post.id
        return mayor + 1

    def crear_post(self, titulo, contenido, autor, tags, estado):
        """
        Crea un Post y lo agrega al blog. Retorna el post creado.
        Lanza ValueError si algún campo está vacío.
        """
        titulo = titulo.strip()
        contenido = contenido.strip()
        estado = estado.strip()

        tags_limpios = []
        for t in tags:
            if t.strip() != "":
                tags_limpios.append(t.strip())

        if titulo == "":
            raise ValueError("el título no puede estar vacío")
        if contenido == "":
            raise ValueError("el contenido no puede estar vacío")
        if len(tags_limpios) == 0:
            raise ValueError("debés ingresar al menos un tag")
        if estado == "":
            raise ValueError("el estado no puede estar vacío")

        nuevo = Post(self._siguiente_id(), titulo, contenido, autor, tags_limpios, estado)
        self.posts.append(nuevo)
        return nuevo

    def to_list(self):
        """Convierte todos los posts en una lista de diccionarios (lista para JSON)."""
        lista = []
        for post in self.posts:
            lista.append(post.to_dict())
        return lista


def crear_autor_desde_dict(datos):
    """
    Reconstruye un objeto Autor desde un diccionario.
    Lanza ValueError si el diccionario está incompleto.
    """
    if not isinstance(datos, dict):
        raise ValueError("los datos del autor deben ser un diccionario")

    for clave in ("nombre", "bio", "especialidad", "redes_sociales"):
        if clave not in datos:
            raise ValueError(f'al autor le falta la clave "{clave}"')

    return Autor(
        datos["nombre"],
        datos["bio"],
        datos["especialidad"],
        datos["redes_sociales"]
    )


def crear_post_desde_dict(datos):
    """
    Reconstruye un objeto Post desde un diccionario.
    Lanza ValueError si el diccionario está incompleto.
    """
    if not isinstance(datos, dict):
        raise ValueError("el post debe ser un diccionario")

    for clave in ("id", "titulo", "contenido", "autor", "tags", "estado"):
        if clave not in datos:
            raise ValueError(f'al post le falta la clave "{clave}"')

    autor = crear_autor_desde_dict(datos["autor"])

    return Post(
        datos["id"],
        datos["titulo"],
        datos["contenido"],
        autor,
        datos["tags"],
        datos["estado"]
    )