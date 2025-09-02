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
# - Dibujar una linea desde el origen hasta el
# - punto (xf, yf)
# ----------------------------------------------------
def draw_line(xf, yf):

    # -- Valor inicial para y
    # -- Comenzamos en el origen
    y = 0

    # -- Valor inicial de D, para decidir que pixel
    # -- encendemos en la columna siguiente: el de arriba
    # -- o el de abajo
    D = -2*yf + xf

    # -- Recorrer todos los pixeles
    for x in range(xf):

        # -- Dibujar pixel actual
        plot(x, y)

        # -- El pixel está por debajo de la linea --> la línea
        # -- está hacia arriba:  Incrementamos 'y' para ir hacia ella
        # -- y calculamos el nuevo D
        if D < 0:  # -- Caso Inclinado
            y = y + 1
            D = D - 2*yf + 2*xf

        else:
            # -- Caso recto
            # -- La y NO se incrementa
            # -- Calcular el siguiente D
            D = D - 2*yf

    # -- Dibujar el punto final
    plot(xf, yf)


# -------------------------------------------
# -- Este algoritmo permite dibujar líneas
# -- en cualquier dirección
# -------------------------------------------
def draw_line2(x0, y0, x1, y1):

    dx = abs(x1-x0)
    dy = -abs(y1-y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx + dy

    while 1:
        plot(x0, y0)

        if (x0 == x1 and y0 == y1):
            break

        e2 = 2*err
        if e2 >= dy:
            err += dy
            x0 += sx
        if e2 <= dx:
            err += dx
            y0 += sy


# -----------
# -- MAIN
# -----------

clear()
draw_line2(0, 0, 15, 2)
mem_refresh()
