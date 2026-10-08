"""
main.py

Archivo principal del sistema del blog. Solo coordina: carga los posts desde
posts.json, crea la instancia de Blog y conecta las opciones del menú con
los métodos de esa instancia.

Ejecutar desde esta carpeta con: python main.py
"""

from blog.datos import cargar_posts, guardar_posts, perfil_autor, estados_post
from blog.menu import mostrar_menu, pedir_datos_nuevo_post
from blog.modelos import Blog, crear_autor_desde_dict
from blog.validaciones import validar_post


def main():
    blog = Blog(cargar_posts())
    cambios_sin_guardar = False

    while True:
        opcion = mostrar_menu()

        if opcion == 1:
            blog.listar_posts()

        elif opcion == 2:
            termino = input("Término a buscar en el título: ").strip()
            if not termino:
                print("\nDebés ingresar un término de búsqueda.")
            else:
                resultados = blog.buscar_por_titulo(termino)
                if resultados:
                    blog.listar_posts(resultados)
                else:
                    print(f'\nNo se encontraron posts con el título "{termino}".')

        elif opcion == 3:
            tag = input("Tag a filtrar: ").strip()
            if not tag:
                print("\nDebés ingresar un tag.")
            else:
                resultados = blog.filtrar_por_tag(tag)
                if resultados:
                    blog.listar_posts(resultados)
                else:
                    print(f'\nNo se encontraron posts con el tag "{tag}".')

        elif opcion == 4:
            titulo, contenido, tags, estado = pedir_datos_nuevo_post()
            try:
                if estado.strip() not in estados_post:
                    raise ValueError(f'el estado "{estado.strip()}" no es válido')
                autor = crear_autor_desde_dict(perfil_autor)
                nuevo = blog.crear_post(titulo, contenido, autor, tags, estado)
                cambios_sin_guardar = True
                print(f'\nPost creado: "{nuevo.titulo}" (id {nuevo.id}). '
                      f'Recordá guardarlo con la opción 6.')
            except ValueError as error:
                print(f"\nNo se pudo crear el post: {error}.")

        elif opcion == 5:
            print("\nValidando posts...\n")
            for post in blog.obtener_posts():
                es_valido, mensaje = validar_post(post)
                if es_valido:
                    print(f"Post {post.id}: válido")
                else:
                    print(f"Post {post.id}: error - {mensaje}")

        elif opcion == 6:
            if guardar_posts(blog.to_list()):
                cambios_sin_guardar = False
                print("\nPosts guardados en posts.json.")

        elif opcion == 7:
            if cambios_sin_guardar:
                respuesta = input("Hay cambios sin guardar. ¿Guardar antes de salir? (s/n): ")
                if respuesta.strip().lower() == "s" and guardar_posts(blog.to_list()):
                    print("Posts guardados en posts.json.")
            print("\n¡Hasta luego!")
            break

        elif opcion is not None:
            print("\nOpción inválida: elegí un número del 1 al 7.")


if __name__ == "__main__":
    main()