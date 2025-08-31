from PIL import Image, ImageDraw


def bresenham_line(draw, x0, y0, x1, y1, color):
    """Dibuja una línea pixel a pixel usando el algoritmo de Bresenham
    (versión simplificada).
    """
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    # Asume que dx > dy y x0 < x1 para esta implementación sencilla.
    # En una implementación completa, se manejarían todos los casos.
    if dx < dy:
        # Aquí se debería manejar la transposición de ejes, pero lo omitimos
        # para simplicidad.
        # Para este ejemplo, solo funcionará si la pendiente es menor que 1.
        return

    p = 2 * dy - dx
    y = y0

    for x in range(x0, x1 + 1):
        draw.point((x, y), fill=color)
        imagen.save('linea_bresenham.png')
        if p >= 0:
            y += 1  # Avanza en y
            p += 2 * dy - 2 * dx
        else:
            p += 2 * dy  # No avanza en y


# --- Configuración de la imagen ---
ancho = 10
alto = 10
imagen = Image.new('1', (ancho, alto), 'white')
lapiz = ImageDraw.Draw(imagen)

# --- Dibujar la línea ---
# Definimos los puntos de inicio y fin
x_inicio, y_inicio = 0, 0
x_fin, y_fin = 3, 1
color_linea = 'black'

# Llamamos a nuestra función personalizada de Bresenham
bresenham_line(lapiz, x_inicio, y_inicio, x_fin, y_fin, color_linea)


# -- Hacer un flip vertical, para mostrar la imagen
# -- con la orientación de los ejes típica en matemáticas
imagen = imagen.transpose(Image.FLIP_TOP_BOTTOM)


# --- Guardar y mostrar la imagen ---
imagen.save('test.png')
# imagen.show()

print("Se ha creado la imagen 'linea_bresenham.png' con una línea "
      "dibujada con el algoritmo de Bresenham.")
