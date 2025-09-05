# -----------------------
# -- CONSTANTES
# -----------------------
# -- Tamaño de la memoria
SIZE_X = 15
SIZE_Y = 5


# -------------------------------
# -- Borrar la pantalla
# -------------------------------
def cls():
    print("\x1b[2J\x1b[H")


# -------------------------------------------------------
# -- Dibujar una linea desde (x0,y0) hasta (x1, y1)
# -- Algoritmo de bresenham optimizado
# -- valido para todos los cuadrantes
# -- Version RENDERIZADO
# -------------------------------------------------------
def bresenham_gen_basic2(x0, y0, x1, y1):

    # -- Distancia en x
    dx = abs(x1 - x0)

    # -- Incremento en eje x
    sx = 1 if x0 < x1 else -1

    # -- Distancia en y
    dy = -abs(y1 - y0)

    # -- Incremento en eje y
    sy = 1 if y0 < y1 else -1

    # -- Error: Distancia del siguiente pixel a la linea
    error = dx + dy

    while True:
        yield (x0, y0)

        e2 = 2 * error

        if e2 >= dy:
            if x0 == x1:
                break
            error = error + dy
            x0 = x0 + sx

        if e2 <= dx:
            if y0 == y1:
                break
            error = error + dx
            y0 = y0 + sy


def render_line(x0, y0, x1, y1):

    # -- Crear el generador
    pixel = bresenham_gen_basic2(x0, y0, x1, y1)

    # -- Obtener el primer pixel del algoritmo
    xa, ya = next(pixel)

    # -- Proceso de rasterizado
    for y in range(SIZE_Y):
        for x in range(SIZE_X):

            # -- Comprobar si el raster es igual al pixel del algoritmo
            if (x, y) == (xa, ya):

                # -- Imprimir el punto en la pantalla
                print('O', end='')

                # -- Calcular el siguiente pixel a renderizar
                try:
                    xa, ya = next(pixel)
                except StopIteration:

                    # -- Devolver punto (0,0). Se ha acabado el renderizado
                    # -- de la linea
                    xa, ya = 0, 0
            else:
                # -- Raster en otro punto: imprimimos un espacio ' '
                print(' ', end='')

        # -- Siguiente linea
        print()


# -----------
# -- MAIN
# -----------
cls()
print('-' * SIZE_X)
render_line(0, 0, 14, 4)
print('-' * SIZE_X)
print()
