from PIL import Image, ImageDraw

# -----------------------------------------------------
# -- Algoritmo de bresenham implementado solo con
# -- aritmetica entera
# -- NO optimizado
# -----------------------------------------------------


# ----------------------------------------------------
# - Dibujar una linea desde el origen hasta el
# - punto (xf, yf)
# ----------------------------------------------------
def draw_line(draw, xf, yf):

    # -- Valor inicial de y
    # -- Comenzamos en el origen
    y = 0

    for k in range(xf):
        print()
        print(f"🟢 Paso {k}:")

        # -- Posicion x actual
        x = k

        print(f"- Punto ({x}, {y})")

        # -- Dibujar pixel actual
        draw.point((x, y))

        # -- Calcular distancia
        # -- D = xf.(2y + 1 ) − 2yf.(xi + 1)
        D = xf * (2*y + 1) - 2*yf*(x + 1)
        print(f"- Distancia: D={D}")

        # -- Determinar el valor de la y del siguiente pixel
        if D < 0:
            # -- Punto debajo de la linea (linea encima)
            # -- Incrementamos la y en 1
            y = y + 1

    # -- Dibujar el punto final
    print()
    print(f"🟢 Paso {xf} (FINAL):")
    print(f"- Punto ({xf}, {yf})")
    draw.point((xf, yf))
    print()


# ------------- Contantes
# -- Tamaño de la pantalla en pixeles
SCREEN_SIZE = (6, 6)

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
