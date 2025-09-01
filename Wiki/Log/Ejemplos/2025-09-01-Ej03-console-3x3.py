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
        print(f'{SIZE_Y-y}│', end='')

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
    print('  ' + cords_x)
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


# ----------------------------------------------------
# - Dibujar una linea desde el origen hasta el
# - punto (xf, yf)
# ----------------------------------------------------
def draw_line(xf, yf):

    # -- Valor inicial de y
    # -- Comenzamos en el origen
    y = 0

    for x in range(xf):

        # -- Dibujar pixel actual
        plot(x, y)

        # -- Calcular distancia del siguiente pixel a la linea
        D = xf * (2*y + 1) - 2*yf*(x + 1)

        # -- Si pixel debajo de la linea, incrementar y
        if D < 0:
            y = y + 1

    # -- Dibujar el punto final
    plot(xf, yf)


# -----------
# -- MAIN
# -----------

clear()
draw_line(2, 0)
mem_refresh()

clear()
draw_line(2, 1)
mem_refresh()

clear()
draw_line(2, 2)
mem_refresh()
