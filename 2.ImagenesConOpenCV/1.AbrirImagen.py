import matplotlib.pyplot as plt
import cv2

imagen=cv2.imread('d:\Yukino.jpg')

print(type(imagen))

print(imagen.shape)
#Error de colores 
#Opencv-> BGR
#Malplot-> RGB
#Cambiamos color
imagen=cv2.cvtColor(imagen,cv2.COLOR_BGR2RGB)
plt.imshow(imagen)


#Leemos con escala de grises y la mostramos en escala de grises
imagenBW=cv2.imread('d:\Yukino.jpg',cv2.IMREAD_GRAYSCALE)
plt.imshow(imagenBW,cmap='gray')
plt.show()
