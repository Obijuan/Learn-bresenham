# -----------------------
# -- CONSTANTES
# -----------------------
# -- Tamaño de la memoria
SIZE_X = 16
SIZE_Y = 12

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
    print('  ┌' + '──' * (SIZE_X-1) + '──┐')
    for y, fila in enumerate(reversed(mem)):

        # -- Inicio de la fila
        print(f'{SIZE_Y-(y+1):02}│', end='')

        # -- Imprimir la fila
        for car in fila:
            print(f"{car}", end='')

        # -- final de fila
        print('│')
    print('  └' + '──' * (SIZE_X-1) + '──┘')

    # -- Obtener la lista de coordenadas x
    # -- Primero el digito de mayor peso
    # dig10 = [f'{i // 10} ' for i in range(SIZE_X)]
    dig10 = [f'{i % 10} ' if i // 10 == 0 else f'{i // 10} '
             for i in range(SIZE_X)]

    dig10 = ''.join(dig10)
    print('    ' + dig10 + ' ')

    # -- Ahora las unidades
    dig1 = ['  ' if i // 10 == 0 else f'{i % 10} ' for i in range(SIZE_X)]

    # -- convertirla a cadena
    dig1 = ''.join(dig1)
    print('    ' + dig1 + ' ')
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
# -- Borrar la pantalla
# -----------------------------------------
def clear():
    for y, line in enumerate(mem):
        for x, _ in enumerate(line):
            mem[y][x] = '⚫'
            # '  '


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
draw_line(11, 0)
mem_refresh()

clear()
draw_line(11, 1)
mem_refresh()

clear()
draw_line(11, 2)
mem_refresh()

clear()
draw_line(11, 3)
mem_refresh()

clear()
draw_line(11, 4)
mem_refresh()

clear()
draw_line(11, 5)
mem_refresh()

clear()
draw_line(11, 6)
mem_refresh()

clear()
draw_line(11, 7)
mem_refresh()

clear()
draw_line(11, 8)
mem_refresh()

clear()
draw_line(11, 9)
mem_refresh()

clear()
draw_line(11, 10)
mem_refresh()

clear()
draw_line(11, 11)
mem_refresh()
