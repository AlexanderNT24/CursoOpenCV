import numpy as np
import cv2

#Creamos la imagen
imagen=np.zeros((500,500,3),np.int8)

#Creamos una funcion para dibujar (evento, coordenadas,etiquetas,paramatros)
def dibujar(evento,x,y,etiquetas, parametros):
    if evento== cv2.EVENT_LBUTTONDOWN:
        cv2.circle(imagen,(x,y),50,(255,0,0),-1)

#Conectamos la funcion con la imagen
#winname="imagen" nombre del frame debe ser el mismo
cv2.namedWindow(winname="imagen")
cv2.setMouseCallback("imagen",dibujar)

#Mostramos la imagen en un bucle infinito, si no se hace asi la ventana se cierra
while True:
    cv2.imshow("imagen",imagen)

    #Si pulsa la tecla escape en ASCII es 27 sale, ambos hacen lo mismo pero no se la diferencia 
    '''if cv2.waitKey(1)==27:
        break'''
    if   cv2.waitKey(10) & 0xFF==27:
        break

#Cuando salga del bucle cierro todas las ventanas
cv2.destroyAllWindows()