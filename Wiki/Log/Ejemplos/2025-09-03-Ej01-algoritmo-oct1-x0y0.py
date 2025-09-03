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
# -- Borrar la pantalla
# -----------------------------------------
def clear():
    for y, line in enumerate(mem):
        for x, _ in enumerate(line):
            mem[y][x] = '⚫'
            # '  '


# ----------------------------------------------------
# - Dibujar una linea desde (x0,y0) hasta (xf, yf)
# - Linea en el 1er octante
# ----------------------------------------------------
def draw_line(x0, y0, xf, yf):

    # -- Valor inicial para y
    y = y0

    # -- Distancia en x
    dx = xf - x0

    # -- Distancia en y
    dy = yf - y0

    # -- Valor inicial de D, para decidir que pixel
    # -- encendemos en la columna siguiente: el de arriba
    # -- o el de abajo
    D = dx - 2*dy

    # -- Recorrer todos los pixeles
    for x in range(x0, xf):

        # -- Dibujar pixel actual
        plot(x, y)

        # -- El pixel está por debajo de la linea --> la línea
        # -- está hacia arriba:  Incrementamos 'y' para ir hacia ella
        # -- y calculamos el nuevo D
        if D < 0:  # -- Caso Inclinado
            y = y + 1
            D = D + 2*dx - 2*dy

        else:
            # -- Caso recto
            # -- La y NO se incrementa
            # -- Calcular el siguiente D
            D = D - 2*dy

    # -- Dibujar el punto final
    plot(xf, yf)


# -----------
# -- MAIN
# -----------

x, y = 5, 4
clear()
draw_line(x, y, x+5, y+0)
mem_refresh()

clear()
draw_line(x, y, x+5, y+1)
mem_refresh()

clear()
draw_line(x, y, x+5, y+2)
mem_refresh()

clear()
draw_line(x, y, x+5, y+3)
mem_refresh()

clear()
draw_line(x, y, x+5, y+4)
mem_refresh()

clear()
draw_line(x, y, x+5, y+5)
mem_refresh()
