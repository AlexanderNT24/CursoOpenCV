import cv2
#En una variable almacenamos la captura que haremos con el opencv 
captura=cv2.VideoCapture(0)
#Del objeto captura usamos el metodo get para obtener al ancho de la ventana
anchoVentana=int(captura.get(cv2.CAP_PROP_FRAME_WIDTH))
#Del objeto captura usamos el metodo get para obtener la altura de la ventana
alturaVentana=int(captura.get(cv2.CAP_PROP_FRAME_HEIGHT))

#Esquina izquierda
x=0
y=0

#Dimensiones del rectangulo a dibujar
#Las dos barras es para que la dibvision nos arroje un entero//
anchoRectangulo=anchoVentana//4
altoRectangulo=alturaVentana//4

while True:
    resultado,video=captura.read()
    #Dibujamos rectangulo
    #cv2.rectangle(donde_dibujar,punto1,punto2,color,grosor)
    cv2.rectangle(video,(x,y),(x+anchoRectangulo,y+anchoRectangulo),color=(255,0,0),thickness=4)
    cv2.imshow('Frame',video)
    if cv2.waitKey(1)==27:
        #Rompo bucle
        break
captura.relase()  
cv2.destroyAllWindows()