# Blog por consola

Sistema interactivo por consola para gestionar publicaciones de un blog.
Permite listar posts, buscar por título, filtrar por tag y validar la
estructura de los posts. Es la versión modular (Módulo 5) del sistema
trabajado en los módulos anteriores.

## Cómo ejecutarlo

1. Tener Python 3 instalado.
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
│
└── blog/
    ├── __init__.py
    ├── datos.py
    ├── menu.py
    ├── operaciones.py
    └── validaciones.py
```

## Responsabilidad de cada archivo

| Archivo | Responsabilidad |
|---|---|
| `main.py` | Archivo principal. Importa las piezas del paquete y coordina el flujo del menú. |
| `blog/__init__.py` | Indica a Python que la carpeta `blog/` es un paquete. Está vacío. |
| `blog/datos.py` | Datos base: `perfil_autor`, `estados_post`, `etiquetas_blog` y `posts`. |
| `blog/menu.py` | Muestra el menú y captura la opción elegida (`mostrar_menu()`). |
| `blog/operaciones.py` | Funciones del blog: `listar_posts()`, `buscar_por_titulo()` y `filtrar_por_tag()`. |
| `blog/validaciones.py` | Reglas de validación de un post (`validar_post()`). |

## Menú del programa

```
--- MENÚ DEL BLOG ---
1. Ver todos los posts
2. Buscar por título
3. Filtrar por tag
4. Validar posts
5. Salir
```

- **1. Ver todos los posts:** muestra título, autor y estado de cada post.
- **2. Buscar por título:** pide un término y muestra los posts cuyo título lo contiene, sin distinguir mayúsculas de minúsculas.
- **3. Filtrar por tag:** pide una etiqueta y muestra los posts que la tienen, sin distinguir mayúsculas de minúsculas.
- **4. Validar posts:** revisa la estructura de cada post e indica cuáles son válidos y cuáles tienen errores.
- **5. Salir:** muestra un mensaje de despedida y termina el programa.

## Nota

El cuarto post de `datos.py` está incompleto a propósito, para poder probar la validación.

## Autor

Egle Aldana Martinelli