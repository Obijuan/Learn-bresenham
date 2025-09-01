# -----------------------
# -- CONSTANTES
# -----------------------
# -- Tamaño de la memoria
SIZE_X = 4
SIZE_Y = 4

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

            # -- El renderizado solo se realiza
            # -- en la zona x <= xf
            if x <= xf:
                # -- Evaluar el punto actual
                D = -2*yf * x + xf * (2*y - 1)

                # -- Si esta por debajo, se renderiza
                if D <= 0:
                    plot(x, y)


# ---------------------------------------------------
# -- Dibujar una linea desde el origien a (xf, yf)
# ---------------------------------------------------
def render_line(xf, yf):

    # -- Raster: recorrer toda la memoria
    for y, line in enumerate(mem):
        for x, _ in enumerate(line):

            # -- El renderizado solo se realiza
            # -- en la zona x <= xf
            if x <= xf:

                # -- Evaluar punto inferior
                DB = -2*yf*x + xf*(2*y - 1)

                # -- Evaluar punto superior
                DT = -2*yf*x + xf*(2*y + 1)

                # -- Comprobar si la linea pasa entre esos
                # -- dos puntos
                if DB < 0 and DT >= 0:
                    # -- Renderizar!
                    plot(x, y)


# -----------
# -- MAIN
# -----------

# -- Linea en 2x2
clear()
render_line(1, 0)
mem_refresh()

clear()
render_line(1, 1)
mem_refresh()

# -- Linea en 3x3
clear()
render_line(2, 0)
mem_refresh()

clear()
render_line(2, 1)
mem_refresh()

clear()
render_line(2, 2)
mem_refresh()

# -- Triangulo en 4x4
clear()
render_line(3, 0)
mem_refresh()

clear()
render_line(3, 1)
mem_refresh()

clear()
render_line(3, 2)
mem_refresh()

clear()
render_line(3, 3)
mem_refresh()

# -- Resultado (Se ha agrupado en horizontal, manualmente)
# -- No es la salida real de la consola (que sale en vertical)

#   ┌────┐   ┌────┐
#  3│    │  3│    │
#  2│    │  2│    │
#  1│    │  1│ *  │
#  0│**  │  0│*   │
#   └────┘   └────┘
#    0123     0123

#   ┌────┐   ┌────┐   ┌────┐
#  3│    │  3│    │  3│    │
#  2│    │  2│    │  2│  * │
#  1│    │  1│  * │  1│ *  │
#  0│*** │  0│**  │  0│*   │
#   └────┘   └────┘   └────┘
#    0123     0123     0123

#   ┌────┐   ┌────┐   ┌────┐   ┌────┐
#  3│    │  3│    │  3│    │  3│   *│
#  2│    │  2│    │  2│   *│  2│  * │
#  1│    │  1│  **│  1│ ** │  1│ *  │
#  0│****│  0│**  │  0│*   │  0│*   │
#   └────┘   └────┘   └────┘   └────┘
#    0123     0123     0123     0123
