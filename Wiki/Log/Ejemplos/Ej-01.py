from PIL import Image, ImageDraw

# Define las dimensiones de la imagen
ancho = 256
alto = 256

# -- Crear imagen
imagen = Image.new('1', (ancho, alto), 'white')

# -- Crear objeto para pintar en la image
lapiz = ImageDraw.Draw(imagen)

# Define la posición y el color del píxel
posicion_pixel = (1, 0)
color_pixel = 'black'

# Dibuja un punto (píxel) en la posición especificada
lapiz.point(posicion_pixel, fill=color_pixel)

# Guarda la imagen como un archivo PNG
imagen.save('pixel_aislado.png')

# Opcional: muestra la imagen
# imagen.show()
