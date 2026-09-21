"""
datos.py

Estructuras de datos base del blog: perfil del autor, estados válidos,
etiquetas y lista de posts.
"""

perfil_autor = {
    "nombre": "Egle Aldana Martinelli",
    "bio": "Estudiante de Data Science y especialista en calidad.",
    "especialidad": "Data Science y Python",
    "redes_sociales": ["@egle_data", "@egle_python"]
}

estados_post = ("borrador", "publicado", "archivado")

etiquetas_blog = {"Data Science", "Python", "Calidad", "Logística", "Python"}

posts = [
    {
        "id": 1,
        "titulo": "Introducción a Data Science",
        "contenido": "Un primer vistazo a la ciencia de datos y sus aplicaciones prácticas.",
        "autor": perfil_autor,
        "tags": ["Data Science", "Principiantes"],
        "estado": "publicado"
    },
    {
        "id": 2,
        "titulo": "Gestión de Calidad en Procesos",
        "contenido": "Métodos para implementar control y aseguramiento de calidad en la industria.",
        "autor": perfil_autor,
        "tags": ["Calidad", "Mejora Continua"],
        "estado": "borrador"
    },
    {
        "id": 3,
        "titulo": "Optimizando la Logística con Datos",
        "contenido": "Cómo el análisis de datos transforma las cadenas de suministro modernas.",
        "autor": perfil_autor,
        "tags": ["Logística", "Data Science"],
        "estado": "archivado"
    },
    {
        # Post incompleto/incorrecto a propósito, para probar validar_post()
        "id": 4,
        "titulo": "",
        "autor": "Autor desconocido",
        "tags": "Python",
        "estado": "en_revision"
    }
]