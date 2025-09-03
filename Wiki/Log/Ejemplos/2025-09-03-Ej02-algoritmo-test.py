# -----------------------
# -- CONSTANTES
# -----------------------
# -- Tamaño de la memoria
SIZE_X = 9
SIZE_Y = 9

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


# -----------------------------------------
# - Dibujar una linea entre dos puntos
# - La linea puede tener cualquier orientacion
# - Todos los valores de entrada deben cumplir
# - que sean >= 0  (no admite numeros negativos)
# - porque la pantalla solo tiene coordenadas positivas
# -----------------------------------------
def draw_line(x0, y0, xf, yf):

    dx = xf - x0
    dy = yf - y0

    if dx >= 0 and dy >= 0:
        # -- Primer cuadrante
        pixel = bresenham_gen_c1(x0, y0, xf, yf)

    elif dx >= 0 and dy <= 0:
        # -- Cuarto cuadrante
        pixel = bresenham_gen_c1(x0, -y0, xf, -yf)

    elif dx <= 0 and dy >= 0:
        # -- Segundo cuadrante
        pixel = bresenham_gen_c1(-x0, y0, -xf, yf)

    else:
        # -- Tercer cuadrante
        pixel = bresenham_gen_c1(-x0, -y0, -xf, -yf)

    while True:
        try:
            x, y = next(pixel)
        except StopIteration:
            return

        if dx >= 0 and dy >= 0:
            plot(x, y)
        elif dx >= 0 and dy <= 0:
            plot(x, -y)
        elif dx <= 0 and dy >= 0:
            plot(-x, y)
        else:
            plot(-x, -y)


# ----------------------------------------------
# - Calcula el siguiente punto de la linea
# - La linea tiene que estar en el PRIMER CUADRANTE
# --------------------------------------------------
def bresenham_gen_c1(x0, y0, xf, yf):

    dx = xf - x0
    dy = yf - y0

    # -- Crear el generador Basico, segun el caso
    if dy > dx:
        # -- Segundo octante
        # -- Se transpone la linea para que este en el
        # -- primer octante
        pixel = bresenham_gen_basic(y0, x0, yf, xf)
    else:
        # -- Primer octante
        # -- Se llama directamente al algoritmo basico
        # -- no se nececista hacer ninguna transformacion
        pixel = bresenham_gen_basic(x0, y0, xf, yf)

    while True:
        try:
            # -- Obtener el punt
            if dy > dx:
                # -- Segundo octante

                # -- Obtener el punto de deshacer la
                # -- transposicion para que este en el segundo
                # -- octante (ya que se habia calcula para el primero)
                y, x = next(pixel)

            else:
                # -- Primer octante
                # -- No hay que aplicar ninguna transformacion al punto
                # -- obtenido
                x, y = next(pixel)
        except StopIteration:
            return

        # -- Devolver el punto calculado
        yield (x, y)


# ----------------------------------------------------
# -- Calcula el siguiente punto de la linea
# -- La linea tiene que estar en el primer octante
# --
# -- Devuelve: El punto calculado
# -----------------------------------------------------
def bresenham_gen_basic(x0, y0, xf, yf):

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
        yield (x, y)

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
    yield (xf, yf)


# -----------
# -- MAIN
# -----------

# -- Centro de la pantalla
cx, cy = 4, 4

# -------- Primer cuadrante

# -- Octante 1
clear()
draw_line(cx, cy, cx+3, cy)
mem_refresh()

clear()
draw_line(cx, cy, cx+3, cy+1)
mem_refresh()

clear()
draw_line(cx, cy, cx+3, cy+2)
mem_refresh()

clear()
draw_line(cx, cy, cx+3, cy+3)
mem_refresh()

# -- Octante 2

clear()
draw_line(cx, cy, cx+2, cy+3)
mem_refresh()

clear()
draw_line(cx, cy, cx+1, cy+3)
mem_refresh()

clear()
draw_line(cx, cy, cx+0, cy+3)
mem_refresh()

# ---------- Segundo cuadrante
clear()
draw_line(cx, cy, cx-1, cy+3)
mem_refresh()

clear()
draw_line(cx, cy, cx-2, cy+3)
mem_refresh()

clear()
draw_line(cx, cy, cx-3, cy+3)
mem_refresh()

clear()
draw_line(cx, cy, cx-3, cy+2)
mem_refresh()

clear()
draw_line(cx, cy, cx-3, cy+1)
mem_refresh()

clear()
draw_line(cx, cy, cx-3, cy+0)
mem_refresh()

# ------------ Tercer cuadrante
clear()
draw_line(cx, cy, cx-3, cy-1)
mem_refresh()

clear()
draw_line(cx, cy, cx-3, cy-2)
mem_refresh()

clear()
draw_line(cx, cy, cx-3, cy-3)
mem_refresh()

clear()
draw_line(cx, cy, cx-2, cy-3)
mem_refresh()

clear()
draw_line(cx, cy, cx-1, cy-3)
mem_refresh()

clear()
draw_line(cx, cy, cx-0, cy-3)
mem_refresh()

# ----------- Cuarto cuadrante
clear()
draw_line(cx, cy, cx+1, cy-3)
mem_refresh()

clear()
draw_line(cx, cy, cx+2, cy-3)
mem_refresh()

clear()
draw_line(cx, cy, cx+3, cy-3)
mem_refresh()

clear()
draw_line(cx, cy, cx+3, cy-2)
mem_refresh()

clear()
draw_line(cx, cy, cx+3, cy-1)
mem_refresh()

clear()
draw_line(cx, cy, cx+3, cy-0)
mem_refresh()
