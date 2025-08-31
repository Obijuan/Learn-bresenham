from PIL import Image, ImageDraw

# -------------------------------------------------
# --- Implementación del algoritmo de Bresenham
# --- para dibujar la línea que termina en (3,1)
# -------------------------------------------------


# ----------------------------------------------------
# - Dibujar una linea desde el origen hasta el
# - punto (xf, yf)
# - Se usa la recta y = 1/3 * x
# ----------------------------------------------------
def draw_line(draw, xf, yf):

    # -- Valor inicial de y
    # -- Comenzamos en el origen
    y = 0

    for k in range(xf):
        print(f"\n* Paso {k}")

        # -- Posicion x actual
        x = k

        print(f"- Pixel actual x={x}, y={y}")

        # -- Dibujar pixel actual
        draw.point((x, y))

        # -- Obtener punto de decision
        xd, yd = x + 1, y + 1/2
        print(f"- Punto de decision: xd={xd}, y={yd}")

        # -- Calcular distancia
        # -- F(x,y) = 3*y - x
        D = 3*yd - xd
        print(f"- Distancia: D={D}")

        # -- Determinar el valor de la y del siguiente pixel
        if D < 0:
            # -- Punto debajo de la linea (linea encima)
            # -- Incrementamos la y en 1
            y = y + 1

    # -- Dibujar el punto final
    draw.point((xf, yf))


# ------------- Contantes
# -- Tamaño de la pantalla en pixeles
SCREEN_SIZE = (5, 5)

# --- Crear una imagen nueva de tipo binario
# --- Solo tiene pixeles blancos y negros
imagen = Image.new('1', SCREEN_SIZE, 'white')

# -- Crear el lapiz. Es el objeto que se usa
# -- para dibujar en la imagen
lapiz = ImageDraw.Draw(imagen)

# -- Dibujar la linea
draw_line(lapiz, 3, 1)

# -- Hacer un flip vertical, para mostrar la imagen
# -- con la orientación de los ejes típica en matemáticas
imagen = imagen.transpose(Image.FLIP_TOP_BOTTOM)

# --- Guardar y mostrar la imagen ---
imagen.save('test.png')
