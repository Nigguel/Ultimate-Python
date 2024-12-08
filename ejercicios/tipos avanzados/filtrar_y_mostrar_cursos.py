"""     Filtrar y Mostrar cursos por estado     """

# Este ejercicio organiza una lista	de cursos en tres grupos según su estado:
# 1. En	progreso.
# 2. Completados.
# 3. No	iniciados.
# El programa debe mostrar cada grupo con un tı́tulo correspondiente.
# Entrada:
#   Una lista de diccionarios, donde cada diccionario tiene las claves:
#       • 'nombre'	(str):	Nombre	del	curso.
#       • 'estado'	(str):	Estado	del	curso.
# Salida:
#   Tres listas separadas según el estado de los cursos.


def organizar_cursos(lista_de_cursos: list) -> str | list:
    """
    Organiza una lista de diccionarios segun su estado

    Args:
    lista_de_cursos (dict): Lista de cursos

    Returns (str | list): imprime las listas
    """
    en_progreso = []
    completado = []
    no_iniciado = []

    for curso in lista_de_cursos:
        if curso["estado"] == "en progreso":
            en_progreso.append(curso["nombre"])
        elif curso["estado"] == "completado":
            completado.append(curso["nombre"])
        else:
            no_iniciado.append(curso["nombre"])

    print("Completado: ")
    for nombre in completado:
        print(f"    -{nombre}")

    print("En progreso: ")
    for nombre in en_progreso:
        print(f"    -{nombre}")

    print("No iniciado: ")
    for nombre in no_iniciado:
        print(f"    -{nombre}")


cursos = [
    {"nombre": "HTML: Sin Fronteras", "estado": "en progreso"},
    {"nombre": "CSS3: Sin Fronteras", "estado": "completado"},
    {"nombre": "SQL: Sin Fronteras", "estado": "no iniciado"},
    {"nombre": "Python: HTML, CSS, Flask, MySQL", "estado": "en progreso"},
    {
        "nombre": "Aprende Javascript, HTML5, CSS3 y NodeJS desde cero",
        "estado": "completado",
    },
    {
        "nombre": "React - Guía definitiva: hooks, router, redux, next + Proyectos",
        "estado": "no iniciado",
    },
    {"nombre": "TypeScript: sin fronteras", "estado": "completado"},
    {"nombre": "Ultimate Python", "estado": "en progreso"},
    {"nombre": "Ultimate Linux", "estado": "completado"},
    {"nombre": "Ultimate Docker", "estado": "no iniciado"},
    {"nombre": "Ultimate GIT + GITHUB", "estado": "en progreso"},
    {"nombre": "Ultimate JavaScript", "estado": "completado"},
    {"nombre": "Ultimate React", "estado": "no iniciado"},
    {"nombre": "Ultimate Java", "estado": "en progreso"},
]

organizar_cursos(cursos)
