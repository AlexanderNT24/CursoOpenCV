import numpy as np
import cv2
#variables globales

dibujando=False
valorX=0
valorY=0

def dibujar(evento,x,y,etiquetas, parametros):
    global dibujando,valorX,valorY

#Cuando hago click
    if evento==cv2.EVENT_LBUTTONDOWN:
        dibujando=True
        valorX=x
        valorY=y
#Cuando muevo el raton haciendo click        
    elif evento==cv2.EVENT_MOUSEMOVE:
        if dibujando==True:
            cv2.rectangle(imagen,(valorX,valorY),(x,y),(255,0,0),-1)
#Cuando suelto el click            
    elif evento==cv2.EVENT_LBUTTONUP:
        dibujando=False
        cv2.rectangle(imagen,(valorX,valorY),(x,y),(255,0,0),-1)           

#Conectamos la funcion con la imagen
#winname="imagen" nombre del frame debe ser el mismo
cv2.namedWindow(winname="imagen")
cv2.setMouseCallback("imagen",dibujar)

#Creamos la imagen
imagen=np.zeros((500,500,3),np.int8)
while True:
    cv2.imshow("imagen",imagen)

    #Si pulsa la tecla escape en ASCII es 27 sale, ambos hacen lo mismo pero no se la diferencia 
    '''if cv2.waitKey(1)==27:
        break'''
    if   cv2.waitKey(10) & 0xFF==27:
        break

#Cuando salga del bucle cierro todas las ventanas
cv2.destroyAllWindows()