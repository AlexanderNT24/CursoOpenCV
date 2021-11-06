import matplotlib.pyplot as plt
import cv2

imagen=cv2.imread('d:\Yukino.jpg')

#Cambiamos color sol para ver
imagen=cv2.cvtColor(imagen,cv2.COLOR_BGR2RGB)

#Cambiar el tamaño (ancho,alto)
imagenRez=cv2.resize(imagen,(600,500))

#Porcentaje de altoy ancho
ratioAncho=0.5
ratioAlto=0.5
imagenRezRatio=cv2.resize(imagen,(0,0),imagen,ratioAncho,ratioAlto)

#Girar imagen X
imagenGiradaX=cv2.flip(imagen,1)

#Girar imagen Y
imagenGiradaY=cv2.flip(imagen,0)

plt.imshow(imagenGiradaY)

#Regresamos al color original
imagenGiradaY=cv2.cvtColor(imagenGiradaY,cv2.COLOR_RGB2BGR)
#Guardar una imagen
cv2.imwrite('d:\Yukinoalrevez.jpg',imagenGiradaY)

plt.show()