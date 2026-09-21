"""
main.py

Archivo principal del sistema del blog. Solo coordina: importa las piezas
del paquete blog y las conecta según la opción que elige el usuario.

Ejecutar desde esta carpeta con: python main.py
"""

from blog.datos import posts
from blog.menu import mostrar_menu
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_post


if __name__ == "__main__":

    while True:
        opcion = mostrar_menu()

        # Si mostrar_menu() retornó None, la entrada no era un número
        if opcion is None:
            continue

        # Opción 1: Ver todos los posts
        if opcion == 1:
            listar_posts(posts)

        # Opción 2: Buscar por título
        elif opcion == 2:
            termino = input("Buscar por título: ").strip()

            if termino == "":
                print("\nLa búsqueda no puede estar vacía.")
            else:
                resultados = buscar_por_titulo(posts, termino)
                if not resultados:
                    print("\nNo se encontraron posts que coincidan con la búsqueda.")
                else:
                    print("\nResultados de la búsqueda:")
                    for post in resultados:
                        print(f"- {post.get('titulo', '(sin título)')}")

        # Opción 3: Filtrar por tag
        elif opcion == 3:
            tag = input("Ingresá la etiqueta a buscar: ").strip()

            if tag == "":
                print("\nEl tag no puede estar vacío.")
            else:
                resultados = filtrar_por_tag(posts, tag)
                if not resultados:
                    print("\nNo se encontraron posts con esa etiqueta.")
                else:
                    print(f"\nPosts con el tag '{tag}':")
                    for post in resultados:
                        print(f"- {post.get('titulo', '(sin título)')}")

        # Opción 4: Validar posts
        elif opcion == 4:
            print("\nValidando posts...\n")
            for i, post in enumerate(posts, start=1):
                es_valido, mensaje = validar_post(post)
                if es_valido:
                    print(f"Post {i}: válido")
                else:
                    print(f"Post {i}: error - {mensaje}")

        # Opción 5: Salir
        elif opcion == 5:
            print("\nGracias por usar el sistema del blog. ¡Hasta luego!")
            break

        # Cualquier otro número no contemplado
        else:
            print("\nOpción inválida, elegí un número entre 1 y 5.")
