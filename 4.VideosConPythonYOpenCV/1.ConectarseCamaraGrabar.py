import cv2
#En una variable almacenamos la captura que haremos con el opencv 
captura=cv2.VideoCapture(0)
#Del objeto captura usamos el metodo get para obtener al ancho de la ventana
anchoVentana=int(captura.get(cv2.CAP_PROP_FRAME_WIDTH))
#Del objeto captura usamos el metodo get para obtener la altura de la ventana
alturaVentana=int(captura.get(cv2.CAP_PROP_FRAME_HEIGHT))
#MAC
#CODIGO FORMATO VIDEO 
#codigo=cv2.VideoWriter_fourcc(*'MJPG')
#Crea un video ('ruta',codigo,fps,(anchoVentana,alturaVentana))
#grabador=cv2.VideoWriter('D:\CursoOpenCV\Videos\video.avi',codigo,20,(anchoVentana,alturaVentana))
#WINDOWS
#CODIGO FORMATO VIDEO 
codigo=cv2.VideoWriter_fourcc(*'DIVX')
#Crea un video ('ruta',codigo,fps,(anchoVentana,alturaVentana))
grabador=cv2.VideoWriter('D:/CursoOpenCV/Videos/video.mp4',codigo,20,(anchoVentana,alturaVentana))

while True:
#Lee captura de pantalla continuamente y se las pasa a la variable video
    resultado,video=captura.read()
    #Grabar
    grabador.write(video)
    #Mostramos
    cv2.imshow('Frame',video)
    #cv2.waitKey(1): Tiempo presionado
    #0xFF==ord('q'): Letra
    #if cv2.waitKey(1) & 0xFF==ord('q')
    #cv2.waitKey(1)==27:ASCII
    if cv2.waitKey(1)==27:
        #Rompo bucle
        break
grabador.relase()   
captura.relase()  
#Destruimos las pantallas 
cv2.destroyAllWindows()
