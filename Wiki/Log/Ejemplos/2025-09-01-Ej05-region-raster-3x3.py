# -----------------------
# -- CONSTANTES
# -----------------------
# -- Tamaño de la memoria
SIZE_X = 3
SIZE_Y = 3

# ------------------------
# -- MEMORIA
# ------------------------
# -- Esta es la memoria de pantalla, con tamaño fijo
mem = [[' ' for _ in range(SIZE_X)] for _ in range(SIZE_Y)]


# ------------------------------------------------------------
# -- Refresco: Dibujar la memoria de pantalla en la consola
# ------------------------------------------------------------
def mem_refresh():

    # -- Imprimir la memoria en la consola
    print()
    print(' ┌' + '─' * (SIZE_X-1) + '─┐')
    for y, fila in enumerate(reversed(mem)):

        # -- Inicio de la fila
        print(f'{SIZE_Y-(y+1)}│', end='')

        # -- Imprimir la fila
        for car in fila:
            print(f"{car}", end='')

        # -- final de fila
        print('│')
    print(' └' + '─' * (SIZE_X-1) + '─┘')

    # -- Obtener la lista de coordenadas x
    cords_x = [str(i) for i in range(SIZE_X)]

    # -- convertirla a cadena
    cords_x = ''.join(cords_x)
    print('  ' + cords_x + ' ')
    print()


# -----------------------------------------
# -- Dibujar un punto en la pantalla
# -----------------------------------------
def plot(x: int, y: int):
    mem[y][x] = '*'


# -----------------------------------------
# -- Borrar la pantalla
# -----------------------------------------
def clear():
    for y, line in enumerate(mem):
        for x, _ in enumerate(line):
            mem[y][x] = ' '


# ---------------------------------------------------
# -- Dibujar un triangulo rectangulo relleno
# -- cuya hipotenusa esta dada por la linea xf,yf
# ---------------------------------------------------
def render_triangle_rect(xf, yf):

    # -- Raster: recorrer toda la memoria
    for y, line in enumerate(mem):
        for x, _ in enumerate(line):

            # -- Evaluar el punto actual
            D = -yf * x + xf * y

            # -- Si esta por debajo, se renderiza
            if D <= 0:
                plot(x, y)


# -----------
# -- MAIN
# -----------

clear()
render_triangle_rect(2, 0)
mem_refresh()

clear()
render_triangle_rect(2, 1)
mem_refresh()

clear()
render_triangle_rect(2, 2)
mem_refresh()
