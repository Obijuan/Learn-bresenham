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


# -----------
# -- MAIN
# -----------

clear()
draw_line(11, 7)
mem_refresh()
