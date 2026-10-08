# Blog por consola

Sistema interactivo por consola para gestionar publicaciones de un blog.
Permite listar posts, buscar por título, filtrar por tag, crear posts nuevos,
validarlos y guardarlos en un archivo JSON, de modo que los datos se conserven
entre ejecuciones del programa.

Esta es la versión con **Programación Orientada a Objetos y persistencia JSON**
(Preentrega 6) del proyecto trabajado en los módulos anteriores.

## Cómo ejecutarlo

1. Tener Python 3 instalado (no se necesitan librerías externas).
2. Abrir una terminal en la carpeta raíz del proyecto (donde está `main.py`).
3. Ejecutar:

```
python main.py
```

El archivo que se ejecuta es **`main.py`**.

## Estructura del proyecto

```
blog_consola/
│
├── main.py
├── README.md
├── posts.json
│
└── blog/
    ├── __init__.py
    ├── datos.py
    ├── menu.py
    ├── modelos.py
    └── validaciones.py
```

## Responsabilidad de cada archivo

| Archivo                | Responsabilidad                                                                                      |
| ---------------------- | ---------------------------------------------------------------------------------------------------- |
| `main.py`              | Punto de entrada. Carga los posts, crea la instancia de `Blog` y conecta el menú con sus métodos.    |
| `posts.json`           | Archivo donde se guardan los posts entre ejecuciones.                                                |
| `blog/__init__.py`     | Indica a Python que la carpeta `blog/` es un paquete.                                                |
| `blog/modelos.py`      | Clases `Autor`, `Post` y `Blog`, y las funciones que reconstruyen objetos desde diccionarios.        |
| `blog/datos.py`        | Datos de referencia (`perfil_autor`, `estados_post`, `etiquetas_blog`) y carga/guardado en JSON.     |
| `blog/menu.py`         | Muestra el menú, captura la opción elegida y pide los datos de un nuevo post.                        |
| `blog/validaciones.py` | Reglas de validación de un objeto `Post` (`validar_post()`).                                         |

## Clases principales

### `Autor`
Representa a la persona que escribe los posts.
- **Atributos:** `nombre`, `bio`, `especialidad`, `redes_sociales`.
- **Método `to_dict()`:** convierte el autor en un diccionario.

### `Post`
Representa una publicación del blog.
- **Atributos:** `id`, `titulo`, `contenido`, `autor`, `tags`, `estado`.
- El atributo `autor` **debe ser una instancia de `Autor`** (composición). Si se
  recibe otro tipo de dato, se lanza un `TypeError`.
- El `estado` es `"borrador"` por defecto.
- **Método `to_dict()`:** convierte el post en un diccionario. Para el autor
  llama al `to_dict()` de `Autor`.

### `Blog`
Centraliza la lógica principal del sistema. Guarda una lista de objetos `Post`
en su atributo `posts`.
- `obtener_posts()`: devuelve todos los posts cargados.
- `listar_posts()`: muestra título, autor y estado (de todos los posts, o de la
  lista que reciba por parámetro).
- `buscar_por_titulo(termino)`: busca ignorando mayúsculas y minúsculas.
- `filtrar_por_tag(tag)`: filtra ignorando mayúsculas y minúsculas.
- `crear_post(...)`: crea un `Post`, lo agrega al blog y lo devuelve. Si algún
  campo está vacío, lanza un `ValueError` con un mensaje claro.
- `to_list()`: convierte todos los posts en una lista de diccionarios.

### Funciones de reconstrucción (en `modelos.py`)
- `crear_autor_desde_dict(datos)`: reconstruye un `Autor` desde un diccionario.
- `crear_post_desde_dict(datos)`: reconstruye un `Post` (con su `Autor`) desde un diccionario.

Ambas lanzan `ValueError` si el diccionario está incompleto.

## Cómo funciona la persistencia JSON

JSON no puede guardar objetos personalizados de Python, por eso hay una
conversión en cada sentido:

```
Guardar:  objeto Post  ->  diccionario  ->  posts.json
Cargar:   posts.json   ->  diccionario  ->  objeto Post
```

**Al guardar (opción 6 del menú):**
1. `Blog.to_list()` llama a `Post.to_dict()` de cada post, que a su vez llama a
   `Autor.to_dict()`. El resultado es una lista de diccionarios.
2. `guardar_posts()` (en `datos.py`) escribe esa lista en `posts.json` con
   `json.dump`. Si recibe algo que no sea una lista de diccionarios, informa el
   error en lugar de intentar guardarlo.

**Al cargar (al iniciar el programa):**
1. `cargar_posts()` (en `datos.py`) lee `posts.json` y lo convierte con `json.loads`.
2. Cada diccionario se convierte en objeto con `crear_post_desde_dict()`, que usa
   `crear_autor_desde_dict()` para reconstruir el autor.
3. `main.py` crea `Blog(posts_cargados)` y todo el menú trabaja sobre esa instancia.

### Manejo de errores
El programa no se cierra inesperadamente en estos casos:
- `posts.json` no existe: se inicia con un blog vacío y el archivo se crea al guardar.
- `posts.json` está vacío: se informa y se inicia con un blog vacío.
- `posts.json` tiene JSON inválido, o no contiene una lista: se informa y se inicia vacío.
- Un post del archivo está incompleto: se omite con un aviso que indica qué clave falta.
- Opción de menú inválida o no numérica: mensaje claro y se vuelve a mostrar el menú.
- Campos vacíos o estado inválido al crear un post: el post no se crea y se indica el motivo.
- Se intenta guardar sin convertir los objetos a diccionarios: se informa el error.

## Menú del programa

```
--- MENÚ DEL BLOG ---
1. Ver todos los posts
2. Buscar por título
3. Filtrar por tag
4. Crear nuevo post
5. Validar posts
6. Guardar posts en JSON
7. Salir
```

- **1. Ver todos los posts:** muestra título, autor y estado de cada post.
- **2. Buscar por título:** pide un término y muestra los posts cuyo título lo contiene.
- **3. Filtrar por tag:** pide una etiqueta y muestra los posts que la tienen.
- **4. Crear nuevo post:** pide título, contenido, tags (separados por coma) y
  estado (`borrador`, `publicado` o `archivado`). El autor es el definido en
  `perfil_autor`. El post se agrega al blog, pero no se escribe en el archivo
  hasta usar la opción 6.
- **5. Validar posts:** revisa cada post e indica cuáles son válidos y cuáles tienen errores.
- **6. Guardar posts en JSON:** escribe los posts actuales en `posts.json`.
- **7. Salir:** si hay cambios sin guardar, pregunta si se quieren guardar antes de salir.

## Qué cambió respecto al checkpoint anterior (Módulo 5)

- Los posts y el autor pasaron de **diccionarios a objetos** (`Post` y `Autor`).
- Se agregó `blog/modelos.py` con las clases `Autor`, `Post` y `Blog`.
- Las funciones `listar_posts`, `buscar_por_titulo` y `filtrar_por_tag` de
  `operaciones.py` pasaron a ser **métodos de la clase `Blog`**, por lo que
  `operaciones.py` se eliminó.
- `datos.py` ya no contiene la lista `posts` escrita en el código: ahora los
  posts se cargan desde `posts.json` y se guardan en ese archivo.
- `validaciones.py` ahora valida objetos `Post` en lugar de diccionarios.
- `main.py` instancia `Blog` y conecta el menú con sus métodos.
- El menú pasó de 5 a 7 opciones: se agregaron **Crear nuevo post** y
  **Guardar posts en JSON**.

## Nota

El cuarto post de `posts.json` es inválido a propósito (título y contenido
vacíos y estado `en_revision`), para poder comprobar que la validación (opción 5)
detecta errores.

## Autor

Egle Aldana Martinelli