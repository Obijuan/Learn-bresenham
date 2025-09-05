# -----------------------
# -- CONSTANTES
# -----------------------
# -- Tamaño de la memoria
SIZE_X = 15
SIZE_Y = 15

# ------------------------
# -- MEMORIA
# ------------------------
# -- Esta es la memoria de pantalla, con tamaño fijo
mem = [[' ' for _ in range(SIZE_X)] for _ in range(SIZE_Y)]


# -------------------------------
# -- Borrar la pantalla
# -------------------------------
def cls():
    print("\x1b[2J\x1b[H")


# ------------------------------------------------------------
# -- Refresco: Dibujar la memoria de pantalla en la consola
# ------------------------------------------------------------
def mem_refresh():

    # -- Imprimir la memoria en la consola
    print()
    print('  ┌' + '──' * (SIZE_X) + '──┐')
    for y, fila in enumerate(reversed(mem)):

        # -- Inicio de la fila
        print(f'{SIZE_Y-(y+1):02}│ ', end='')

        # -- Imprimir la fila
        for car in fila:
            print(f"{car}", end='')

        # -- final de fila
        print(' │')
    print('  └' + '──' * (SIZE_X) + '──┘')

    # -- Obtener la lista de coordenadas x
    # -- Primero el digito de mayor peso
    # dig10 = [f'{i // 10} ' for i in range(SIZE_X)]
    dig10 = [f'{i % 10} ' if i // 10 == 0 else f'{i // 10} '
             for i in range(SIZE_X)]

    dig10 = ''.join(dig10)
    print('     ' + dig10 + ' ')

    # -- Ahora las unidades
    dig1 = ['  ' if i // 10 == 0 else f'{i % 10} ' for i in range(SIZE_X)]

    # -- convertirla a cadena
    dig1 = ''.join(dig1)
    print('     ' + dig1 + ' ')
    print()


# -----------------------------------------
# -- Dibujar un punto en la pantalla
# -----------------------------------------
def plot(x: int, y: int):
    mem[y][x] = '🟢'
    # '██'
    # '●'
    # '•'
    # '⭕'
    # '█'


# -----------------------------------------
# -- Borrar la memoria de pantalla
# -----------------------------------------
def mem_clear():
    for y, line in enumerate(mem):
        for x, _ in enumerate(line):
            mem[y][x] = '⚫'
            # '  '


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
    for x in range(SIZE_X):
        for y in range(SIZE_Y):

            # -- Comprobar si el raster es igual al pixel del algoritmo
            if (x, y) == (xa, ya):

                # -- En la posicion actual del raster hay que dibujar un punto
                plot(x, y)

                # -- Calcular el siguiente pixel a renderizar
                try:
                    xa, ya = next(pixel)
                except StopIteration:
                    return


# -----------
# -- MAIN
# -----------
mem_clear()
cls()
render_line(0, 0, 14, 2)
mem_refresh()
