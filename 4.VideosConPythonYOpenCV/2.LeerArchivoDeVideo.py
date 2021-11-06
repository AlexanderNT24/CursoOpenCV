import cv2

#En una variable almacenamos la captura que haremos con el opencv
#0 para stream de webcam y 'ruta' para un video del dispositivo o de alguna fuente
captura=cv2.VideoCapture('D:/CursoOpenCV/Videos/video.mp4')

#Verificamos si se a abierto
if captura.isOpened()==False:
    print("Error al abrir el fichero de video")

while captura.isOpened():
    resultado,video=captura.read()
    if resultado:
       cv2.imshow('Frame',video)
       
       #cv2.waitKey(1): Tiempo presionado
       #0xFF==ord('q'): Letra
       #if cv2.waitKey(1) & 0xFF==ord('q')
       #cv2.waitKey(1)==27:ASCII
       if cv2.waitKey(1)==27:
           #Rompo bucle
           break
    else: 
        break    
captura.relase()
cv2.destroyAllWindows()    