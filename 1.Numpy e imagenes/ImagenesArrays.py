import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

imagen=Image.open('d:\Yukino.jpg')

print(type(imagen))

print(imagen.size)

arrayImagen=np.asarray(imagen)

#print(arrayImagen)
print(arrayImagen.shape)
#[:,:,0]=todas la filas y columnas
arrayImagen[:,:,0]
plt.imshow(arrayImagen)
plt.show()
